#!/bin/bash

# tries to run python code
# if it does not run succesfully, goes to browser

#python 00_flat_world.py || python -mwebbrowser http://127.0.0.1:8000/walking_camera/basic_world.html

#python "$1" || start http://127.0.0.1:8000/walking_camera/basic_world.html

if [[ "$1" == "" ]]; then
	echo "enter a file name"
	echo "usage: ./run.sh filename"
elif [[ "$OSTYPE" == "msys" ]]; then
	echo "Hello Windows User"
	python "$1" || (echo "opening browser..."; start http://127.0.0.1:8000/walking_camera/basic_world.html)
elif [[ "$OSTYPE" == "darwin" ]]; then
	echo "Hello Mac User"
	python "$1" || (echo "opening browser..."; open http://127.0.0.1:8000/walking_camera/basic_world.html)
elif [[ "$OSTYPE" == "linux" ]]; then
	echo "Hello Linux User"
	python "$1" || (echo "opening browser..."; xdg-open http://127.0.0.1:8000/walking_camera/basic_world.html)
elif False; then
	echo "chrome call here"
else
	echo "Unsupported OS: $OSTYPE"
fi