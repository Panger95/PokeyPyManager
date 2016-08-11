<font color=red size=4>***LATEST COMMIT REQUIRES YOU TO RUN PIP INSTALL -R REQUIREMENTS.TXT AGAIN :)***</font>


PokeyPy Manager
============

PokeyPy Manager is a tool which allows you to manage your Pokemon in Pokemon Go. It utilizes https://github.com/rubenvereecken/pokemongo-api to gather information and to perform management actions
such as releasing/evolving/renaming Pokemon.

<b>DISCLAIMER: Since this interacts with the PoGo servers to fetch data / perform evovlves/releases/renames, it is possible to be banned. If you are not comfortable with this possibility, please do not use this tool</b>

Features
--------

- View all your Pokemon, including their IVs and CP level
- Rename Pokemon to include IV in name
- See stats for your trainer, including capture rate and distance walked
- Batch release and evolve Pokemon

Requirements
------------

- [Python 2.7](https://www.python.org/downloads/release/python-2712/)


Instructions
------------
- Install Python 2.7 from the link above
- Open Command Prompt/Terminal/equivalent
- Navigate to the root of the PokeyPySnipe directory
- Run ```pip install -r requirements.txt```
- Navigate to the ```pogo``` directory
- Duplicate ```config.ini.example``` and rename it to ```config.ini```, edit it with your options
- Run ```python mgr.py```
- Open http://127.0.0.1:5100 in your browser

Troubleshooting
---------------
- On Windows, you may need to copy requirements.txt to ```C:/python27/scripts``` to be able to run ```pip install```
- On Windows, you may receive the error ```failed to build xxhash```. If this happens, install the Microsoft Visual C++ Compiler for Python 2.7 from https://www.microsoft.com/en-us/download/details.aspx?id=44266

--------------


Thanks to https://github.com/rubenvereecken/pokemongo-api for providing the API used by PokeyPy Manager, and to all the developers who worked on the Unknown6 solution - PokeyPy Manager uses the encrypt dll/so files from http://pgoapi.com.


Here's a screenshot of it in action:

<img src="http://i.imgur.com/rL1yd5D.png">
