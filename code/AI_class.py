from __future__ import division

import random
import time

class AI:
    def __init__(self):

        # mode: follow, run, or none
        self.mode = "none"

        # status: active or not
        self.status = False

        # keep track of last movement
        self.count = 15

    def follow(self, xm, zm, x, z):
        '''
            guide the AI away from given coordinates
            xm and ym are current position, x and z are player position
        '''
        move = [False, False, False, False]
        dist = [(xm - x), (zm - z)]
        if dist[0] > 1.25:
            move[2] = True
        elif dist[0] < -1.25:
            move[3] = True
        if dist[1] > 1.25:
            move[1] = True
        elif dist[1] < -1.25:
            move[0] = True

        return move
    
    def run_away(self, xm, zm, x, z):
        '''
             make AI run from these x z coordinates
        '''
        move = [False, False, False, False]
        dist = [(xm - x), (zm - z)]
        if dist[0] < 0 and dist[0] > -3:
            move[2] = True
        elif dist[0] > 0 and dist[0] < 3:
            move[3] = True
        if dist[1] > -3 and dist[1] < 0:
            move[1] = True
        elif dist[1] < 3 and dist[1] > 0:
            move[0] = True

        return move

class Creeper(AI):
    def __init__(self, world):
        # place creeper randomly in world
        sign = random.choice([-1, 1])
        x = sign * random.randint(30, 60)
        sign = random.choice([-1, 1])
        z = sign * random.randint(30, 60)
        y = -1
        # prevent collisions with existing blocks
        while (x, y, z) in world:
            y += 1
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z

        # want to head towards ship
        self.target = (10, 0, 2) #approximate center of ship

        # how often this creeper moves
        # fewer frames means faster movement
        self.frames = random.randint(15, 40)

        self.count = 0

        self.mode = "follow"

        self.status = False

        self.ai = AI()

        self.timer = ""

    def follow(self, world):
        # the Creeper follow uses the AI follow with the
        # locally stored coordinates

        # get basic direction(s) to move
        direc = self.ai.follow(self.pos_x, self.pos_z, self.target[0], self.target[2])
        # make moves in that direction accounting for y and other blocks
        move = False
        if direc[0]:
            pos = self.avail_direc(world, "z")
            if pos:
                self.pos_z = pos[2]
                self.pos_y = pos[1]
                move = True
        elif direc[1]:
            pos = self.avail_direc(world, "-z")
            if pos:
                self.pos_z = pos[2]
                self.pos_y = pos[1]
                move = True
        if direc[2]:
            pos = self.avail_direc(world, "-x")
            if pos:
                self.pos_x = pos[0]
                self.pos_y = pos[1]
                move = True
        elif direc[3]:
            pos = self.avail_direc(world, "x")
            if pos:
                self.pos_x = pos[0]
                self.pos_y = pos[1]
                move = True
        while (self.pos_x, self.pos_y - 1, self.pos_z) not in world:
            self.pos_y -= 1
            move = True

        # if want to move, but can't: move a random direction
        if any(direc) and not move:
            d = random.choice(["x", "-x", "z", "-z"])
            pos = self.avail_direc(world, d)
            if pos:
                self.pos_x = pos[0]
                self.pos_y = pos[1]
                self.pos_z = pos[2]
                while (self.pos_x, self.pos_y - 1, self.pos_z) not in world:
                    self.pos_y -= 1

    # if can move that direction, returns new position
    # otherwise returns False
    # assumes Creeper can jump two blocks instead of just one
    def avail_direc(self, world, direc):
        pos = (self.pos_x, self.pos_y, self.pos_z)
        if direc == "x":
            pos = (pos[0] + 1, pos[1], pos[2])
        elif direc == "-x":
            pos = (pos[0] - 1, pos[1], pos[2])
        elif direc == "z":
            pos = (pos[0], pos[1], pos[2] + 1)
        elif direc == "-z":
            pos = (pos[0], pos[1], pos[2] - 1)

        if pos in world or (pos[0], pos[1] + 1, pos[2]) in world:
            pos = (pos[0], pos[1] + 1, pos[2])
            if pos in world or (pos[0], pos[1] + 1, pos[2]) in world:
                pos = (pos[0], pos[1] + 1, pos[2])
                if pos in world or (pos[0], pos[1] + 1, pos[2]) in world:
                    return False
        return pos

    def explode(self):
        if isinstance(self.timer, str):
            self.timer = time.time()
            return "5"
        elif (time.time() - self.timer) > 5:
            return "boom"
        elif (time.time() - self.timer) > 4:
            return "1"
        elif (time.time() - self.timer) > 3:
            return "2"
        elif (time.time() - self.timer) > 2:
            return "3"
        elif (time.time() - self.timer) > 1:
            return "4"
