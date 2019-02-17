==========================
Frequently Asked Questions
==========================

What version of Python is required?
-----------------------------------

SensorCraft currently supports Python 2.7 and Python 3.X.  We have tested 
the software with Enthought Canopy version 1.7.x and Enthought Canopy 
version 2.1.3 which supports both Python 2.7 and Python 3.5.  Please make sure
you download and install the correct version of Python on your computer so
SensorCraft will run.  The `install section of the guide 
<http://sensorcraft.readthedocs.io/en/latest/intro.html#install>`_ has all 
the details and steps you through installing Enthought Canopy with 
Python 2.7 or Python 3.X.

`Wiki <https://wiki.python.org/moin/Python2orPython3>`_ provides more information on the general differences and advantages between Python 2.7 and 3.X.

Error "AttributeError: 'Window' object has no attribute 'label'"
----------------------------------------------------------------

This is an error that is caused by undefined interactions between Enthought
Canopy and Pyglet.  A workaround is to restart your kernel before running
each SensorCraft exercise. See the `SensorCraft guide
<http://sensorcraft.readthedocs.io/en/latest/intro.html#restart-of-the-python-kernel>`_ for how to do this.

Error "IOError: [Errno 2] No such file or directory: 'texture.png'"
-------------------------------------------------------------------

This usually happens because you are trying to run a SensorCraft program without being in the code directory.  The `changing directory section of the guide
<http://sensorcraft.readthedocs.io/en/latest/intro.html#changing-directory>`_
explains how to navigate to the correct directory.

Error "NameError: name 'xrange' is not defined"
-----------------------------------------------

This error should no longer appear as it was fixed when we ported the code
to support Python 3.X.  If you see this error please make sure you
have the latest version of code and run the program again. The `install section of 
the guide <http://sensorcraft.readthedocs.io/en/latest/intro.html#install>`_ 
steps you through installing Enthought Canopy with Python 2.7 and/or
Python 3.5 support.


Error "ImportError: cannot import name gl_info"
-----------------------------------------------

This error occurs when you are not running the correct version of pyglet.
To ensure you have the correct updated version, please see the guide's `install section <http://sensorcraft.readthedocs.io/en/latest/intro.html#install>`_.


Can I play SensorCraft on my tablet?
------------------------------------

Unfortunately not yet. Hopefully in the near future SensorCraft will work on
tablets.  

Can I play SensorCraft on a Raspberry Pi?
-----------------------------------------

Unfortunately not yet. Hopefully in the near future SensorCraft will work on
the Raspberry Pi platform.

I have fallen off the edge of the world what do I do?
-----------------------------------------------------

Simply press the Y key on your keyboard and you shall be transported back 
to spawn.

Common Programming Errors 
--------------------------

*Wrong Directory*
=================

You must be in the correct directory in order to run your code. To check 
the directory that you are in, run the command \"pwd\", which will print 
your working directory to the command promt. In order to run your code, 
you have to be in the folder that contains the file that your code is 
stored in. For example, if your code is stored under the filename 
\"code_file.py\", and stored in a folder named \"code_folder\", then 
your working directory must end in \"code_folder/\", in order for your 
code to run. 

If you get an error message that looks like this:

``ERROR:root:File \`'00_flat_world.py\'` not found.``

That probably means that you are in the wrong working directory. To get to 
the correct directory, type in to your console ``cd`` which will take you 
back to your default directory and print your current location. It should look something like this, with your name instead of "user_name":

``C:\Users\user_name\``

However, you're not in the SensorCraft code folder, so type the following
into your console. Keep in mind, you may need to adjust the location 
slightly depending on the location of your SensorCraft folder.

``cd Desktop/SensorCraft/Code`` 

and you should get an output that looks like this:

``C:\Users\user_name\Desktop\SensorCraft\Code``

Now that you are in the correct directory, try running your code again by 
typing the command:

``%run 00_flat_world.py`` 

and you shouldn't get an error message.

*Kernel Restart*
=================

Due to an error in the Canopy application, you can only run the program 
once per every restart of your console, or kernel. If you get an error 
code that ends like this:

.. code-block:: python

	C:\Users\user_name\Desktop\SensorCraft\code\00_flat_world.py in on_resize(self, width, height)
    	763         """
    	764         # label
	--> 765         self.label.y = height - 10
    	766         # reticle
    	767         if self.reticle:
	AttributeError: 'Window' object has no attribute 'label'

That means that you need to restart your kernel in order to run your  
program again. To do this, you can either do ``ctrl + .``, or, form the 
top of the Canopy interface, you can select Run > Restart Kernel.... You
should get a popup asking you if you are sure you would like to restart
the kernel, press ``Restart``.

You should get a message like this in your kernel: 

.. code-block:: python

	Welcome to Canopy's interactive data-analysis environment!
	Kernel running in the 'User' environment.
	Pylab is active using TkAgg.
	Python 3.5.2 |Enthought, Inc. (x86_64)| (default, Mar  2 2017, 16:37:47) 
	[MSC v.1900 64 bit (AMD64)]
	In [1]:

Once you get this message, you should be able to run your code without 
another error message. 