05 Saving the World
-------------------

SensorCraft makes it fun to build objects in your world but we currently have
no way to save them for use in other worlds.  For this exercise, we are going
to add some new textures and create a new method that will save the world so 
we can reload it in the future.  The blocks we are going to add will be state
of the art `United States Air Force (USAF) <https://www.usmilitary.com/>`_ 
created blocks that are made out of composite material.  Composites are now 
used in aircraft like the F22 Stealth Fighter and commercial aircraft. To get 
started with this programming exercise, first copy the file
03_show_current_block_TVR.py python code to a new file 
05_saving_the_world_TVR.py but replace TVR with your initials using the
following command::

    cp 03_show_current_block_TVR.py 05_saving_the_world_TVR.py

First, delete lines 77 - 87 as we no longer need the numbered stone blocks. 
Next we need to change the file name used for textures on line 76 change the
line to ``TEXTURE_PATH = 'composite_textures.png'``.  
At line 82 you want to add the new composite blocks so after all the changes
above line 76 - 89 should look like the following chunk of code:

.. literalinclude:: ../code/05_saving_the_world.py
    :lines: 76-89

Next, we need to remove the code that placed the numbered stone blocks to
form the number lines on the axis in exercise 3.  Your ``_initialize`` method
should look like the following after all the code has been deleted:

.. literalinclude:: ../code/05_saving_the_world.py
    :pyobject: Model._initialize

We now have to add the new composite blocks to our character's inventory. To do so, modify line 490 so it looks like the following:

.. literalinclude:: ../code/05_saving_the_world.py
    :lines: 489-490

Recall back to the exercise `03_show_current_block <03_show_current_block.html>`__ 
and consider what modifications need to be made to the ``draw_label`` method.  
Within the if/else block, you need to make adjustments for the new composite 
blocks that we added your new ``draw_label`` method should be something like:

.. literalinclude:: ../code/05_saving_the_world.py
    :pyobject: Window.draw_label

How do we tell the game that it can save the world?  We could spend time and
write a complicated menu system that lets a user enter a file name, but since
we are just starting out lets deploy a simple solution.  One simple solution
is to simply press a key, in this case the ``O`` key and the method save_txt
will be called from the model class.  Below is what the new on_key_press method
will look like, take note of the last elif:

.. literalinclude:: ../code/05_saving_the_world.py
    :pyobject: Window.on_key_press

Finally, we implement the method that will save our world, or parts of the 
world we care about.  First a little background: Python has this incredibly
powerful data structure called a dictionary.  Dictionaries allow a programmer
to associate a key to any given value.  In our case the key is ``X``, ``Y``, 
``Z`` position of the block and the value is the type of block like 
``COMPOSITE_RED``, ``COMPOSITE_BLUE``, ``COMPOSITE_BLACK``, ``SAND``, 
``GRASS``, ``BRICK``, etc. You can learn more about dictionaries in Python by reading the `data structure dictionary documentation page
<https://docs.python.org/3.5/tutorial/datastructures.html#dictionaries>`_.  

Go to line 88 where you defined textured blocks and add another line as below::

	COMPOSITE = [COMPOSITE_RED, COMPOSITE_BLUE, COMPOSITE_BLACK,
	COMPOSITE_GREY, COMPOSITE_GREEN]

The code should look like below:

.. literalinclude:: ../code/05_saving_the_world.py
    :lines: 76-90

This creates a list that has all the types of composite blocks. These are 
the only types of blocks we are interested in saving, you could easily
add more blocks to the list as is required for your game. 

We want the file we save to to be as small as possible so we can share our
saved worlds with friends. Let's think about the necessary information 
needed to define a block. Every block has a location in the world in the
form x, y, z and a texture that defines how it looks. We have an indexed list
defining the textures so each composite block type has a corresponding number. 
As we defined it, we can say ``COMPOSITE[0]`` corresponds to ``COMPOSITE_RED``, 
COMPOSITE[1] is ``COMPOSITE_BLUE``, and so on through the end of the list. 
Hence we can store each block as four numbers: x, y, and z coordinates and the
number corresponding to the index in the list that has the block's texture.

Let's use this logic to write a new function that translates between the literal 
texture type and the numerical equivalence in the ``COMPOSITE`` list. At the end of 
the model class copy and paste the below function.

.. literalinclude:: ../code/05_saving_the_world.py
    :pyobject: Model.get_block_index

This function behaves slightly differently than previous methods we've implemented. 
In the first line we have two parameters ``num="", type=""``, but notice the 
parameters are set equal to default values. So if you make a call to the function as 
just ``model.get_block_index()``, these variables will default to ``""``, n 
empty string. The function ``isinstance`` is a way of checking the type of 
object. So now if we walk through the function, we can see that it checks if 
``num`` is an integer and if it is, returns the texture at that index in the 
``COMPOSITE`` list. If instead the ``type`` argument is provided (the specific
texture), the function will return the corresponding integer index.

Now let's add the function that actually writes to an external file to save our 
blocks. Just above ``get_block_index``, add the following.

.. literalinclude:: ../code/05_saving_the_world.py
    :pyobject: Model.save_txt

This function finds all the composite blocks in the world and writes the 
position and texture type as an integer to a file called
``composite_world.txt``. If you open this file, you will see lines with four 
numbers on them, the first three corresponding to a block's position and the 
last the index of the block's texture.  Run the program with IDLE then place a
few red composite bricks, finally push the ``O`` key (not the zero key but the
O key) to save the composite blocks to a file called ``composite_world.txt`` so
we can use the file in the next chapter to load a saved world.  You can now 
share these save files with friends via email attachment.
