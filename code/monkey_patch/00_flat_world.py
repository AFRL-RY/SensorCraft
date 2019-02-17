from __future__ import division
import sys
import math
import random
import time

from pyglet.gl import *

# our custom file we which is monkey patched below
# so students edit code here instead of in giant file
import base

def _initialize(self):
    print("new initialize")
    """ Initialize the world by placing all the blocks.

    """
    n = 80  # 1/2 width and height of world
    s = 1  # step size
    y = 0  # initial y height
    for x in range(-n, n + 1, s):
        for z in range(-n, n + 1, s):
            # create a layer stone an grass everywhere.
            self.add_block((x, y - 2, z), base.GRASS, immediate=False)
            self.add_block((x, y - 3, z), base.STONE, immediate=False)
            if x in (-n, n) or z in (-n, n):
                # create outer walls.
                for dy in range(-2, 3):
                    self.add_block((x, y + dy, z), base.STONE, immediate=False)

    # generate the hills randomly
    o = n - 10
    for _ in range(120):
        a = random.randint(-o, o)  # x position of the hill
        b = random.randint(-o, o)  # z position of the hill
        c = -1  # base of the hill
        h = random.randint(1, 6)  # height of the hill
        s = random.randint(4, 8)  # 2 * s is the side length of the hill
        d = 1  # how quickly to taper off the hills
        t = random.choice([base.GRASS, base.SAND, base.BRICK])
        for y in range(c, c + h):
            for x in range(a - s, a + s + 1):
                for z in range(b - s, b + s + 1):
                    if (x - a) ** 2 + (z - b) ** 2 > (s + 1) ** 2:
                        continue
                    if (x - 0) ** 2 + (z - 0) ** 2 < 5 ** 2:
                        continue
                    self.add_block((x, y, z), t, immediate=False)
            s -= d  # decrement side lenth so hills taper off

base.Model._initialize = _initialize

def main():
    window = base.Window(width=800, height=600, caption='Sensor Craft', resizable=True)
    # Hide the mouse cursor and prevent the mouse from leaving the window.
    window.set_exclusive_mouse(True)
    base.setup()
    pyglet.app.run()


if __name__ == '__main__':
    main()
