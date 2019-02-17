from __future__ import division
import sys
import math
import random
import time

from collections import deque
from pyglet import image
from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse

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

base.Model._initialize = _initialize

def on_key_press(self, symbol, modifiers):
    """ Called when the player presses a key. See pyglet docs for key
    mappings.

    Parameters
    ----------
    symbol : int
        Number representing the key that was pressed.
    modifiers : int
        Number representing any modifying keys that were pressed.

    """
    if symbol == key.W:
        self.strafe[0] -= 1
    elif symbol == key.S:
        self.strafe[0] += 1
    elif symbol == key.A:
        self.strafe[1] -= 1
    elif symbol == key.D:
        self.strafe[1] += 1
    elif symbol == key.SPACE:
        if self.dy == 0:
            self.dy = JUMP_SPEED
    elif symbol == key.ESCAPE:
        self.set_exclusive_mouse(False)
    elif symbol == key.Y:
        self.position = (0, 0, 0)
        dx, dy, dz = self.get_motion_vector()
        self.dy = 0
    elif symbol == key.TAB:
        self.flying = not self.flying
    elif symbol in self.num_keys:
        index = (symbol - self.num_keys[0]) % len(self.inventory)
        self.block = self.inventory[index]
    elif symbol == key.B:
        self.build_wall()

base.Window.on_key_press = on_key_press

def build_wall(self):
    """ Builds a simple wall

    """
    for x in range(-10, 10):
        self.model.add_block((x, -1, -10), base.STONE)
        self.model.add_block((x, 0, -10), base.STONE)
        self.model.add_block((x, 1, -10), base.STONE)
    print("built wall")

base.Window.build_wall = build_wall

def main():
    window = base.Window(width=800, height=600, caption='Sensor Craft', resizable=True)
    # Hide the mouse cursor and prevent the mouse from leaving the window.
    window.set_exclusive_mouse(True)
    base.setup()
    pyglet.app.run()


if __name__ == '__main__':
    main()
