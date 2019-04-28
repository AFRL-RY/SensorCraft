=============
00 Flat World
=============

In this exercise, we will modify the original code downloaded to get rid of 
everything but a flat world with a one-block-high "fence" around the perimeter.
We created this `YouTube video about about chapter 00 Flat World 
<https://youtu.be/dsLC7CDM0hg>`_

To get started with this programming exercise, first copy the original game's 
python code to a new file 00_flat_world_TVR.py but replace "TVR" with your 
initials using the following command::

	cp main.py 00_flat_world_TVR.py

Unix based operating systems such as Linux and MacOS use the command "cp" to
copy a file while Windows uses the "copy" command. Make the appropriate change
based on your operating system.  Another option is to use a graphical file
manager to copy the file such as File Explorer (Windows) or Finder (MacOS).

The object called "Model" starting on line 128 contains all the information
about the world and the blocks that were used to create it.  A method named
"_initialize" is used to create the world which initially is flat with a stone
fence around it, and is contained in lines 157 to 192.
Then starting on line 174 
and continuing until line 192, random hills are generated. To keep the world flat, 
simply comment out that block
of code from line 174 to line 192 by placing a '#' on the first character of each
line. Below is what the _initalize method will look like after the code is
"commented out".

.. literalinclude:: ../code/00_flat_world.py
	:pyobject: Model._initialize

The controls in SensorCraft are similar to most PC video games. Use ``w`` 
to move forward, ``a`` to move left, ``d`` to move right, ``s`` to move 
backwards, and ``space bar`` to jump. There are some other controls that 
let you manipulate your environment as well. If you left-click on your 
mouse, you will remove the block that you're pointing at. If you 
right-click, you will place one block. Right now, you will only be able 
to place blocks of bricks, but, later in the guide, you will learn how 
to change the type of block you are placing. 

When you run your program, the movement of your pointer will be constricted
to only in-game use, and you will not be able to click anything outside of 
the game-play window that appears on your computer. If you wish to leave 
the gameplay window, you must first press ``esc`` which will allow you to 
move your pointer around outside of the gameplay window. To resume control 
of your character in the game, simply click anywhere in the gameplay window
and the movement of your pointer will, again, be constricted to only in-game
use. 

Now run the program "python 00_flat_world_TVR.py".  Then walk in a straight 
line and eventually you will run into a stone wall that is four blocks high.
This stone wall is meant to represent the end of the world, if you go over the
wall Dr. Steve will fall forever.  If you do fall out of the world you can
press the 'Y' key and you will be transported back to position 0,0,0. 

Now, it is important to change the name of our game to SensorCraft. Skip down to
line 891 and change the caption parameter from "Pyglet" to "SensorCraft". 
Test your title change by running the program once again "python
00_flat_world_tvr.py",  then make sure the title has been changed.

.. literalinclude:: ../code/00_flat_world.py
	:pyobject: main