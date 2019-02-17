06 Loading the World
====================

This exercise builds on the previous exercise named 05_pickling_the_world_TVR. Be
sure to complete the previous exercise before you attempt this exercise.  

Here we will practice reading in the file of a previously saved world. This is
helpful in the event that you create a super cool world and want to save it for
future use or share with friends.  The code presented in this exercise will 
assume the file to read is called "composite_world_TVR.txt" and that the file 
exists.  If this file does not exist the method will fail.

To get started with this programming exercise first copy the file 05_saving_the_world_TVR.py python code to
a new file  06_loading_the_world_TVR.py but replace TVR with your initials using
the following command::

    cp 05_saving_the_world_TVR.py 06_loading_the_world_TVR.py

In this new file, jump down to line 421, just below the process_entire_queue 
function, and create a new method called ``load_txt`` which will read a text file 
created from the previous chapter 
`05_saving_the_world <05_saving_the_world.html>`__.  The ``load_txt`` method calls
the add_block method for each new block. The new ``load_txt`` method is shown below:

.. literalinclude:: ../code/06_loading_the_world.py
    :pyobject: Model.load_txt

The last thing we need to do is modify the method ``on_key_press`` so when the
"L" key is pressed which will call the ``load_txt`` method.  The new 
``on_key_press`` method is listed below:

.. literalinclude:: ../code/06_loading_the_world.py
    :pyobject: Window.on_key_press

Testing Load and Save
---------------------
We should now be able to save and load a world with the changes suggested 
above.  Let's test this out before moving on. First, run the program 
``05_loading_the_world.py``  in IDLE, then make some simple changes to the 
world.  Recall that the save and load methods will only account for COMPOSITE
blocks, so if you build something out of grass, you won't be able to save it.
Walk around a while and try adding a few composite blocks to the world.

Once you have customized the world, press "O" to save the world.  Close the 
window and then run the program again.  Any changes you have made will be gone!
Now we want to load the world you had made by pressing "L".  This should load 
the world that you had previously made.