# Shadow Shark Listener
A full fledged reverse TCP handler used to interact with Shadow Shark payloads written in pure python3.

## Installation
### Debian
```
$ sudo apt-get install python3 git
$ git clone https://github.com/MrSharkSpamBot/Shadow-Shark-Listener.git
```

## Usage
Note this tool is meant to be used for ethical purposes if you plan to use this for unethical purposes then do not download this tool and leave this page immediately. This tool is designed to be used on Linux but should be able to work on most other operating systems. Running the tool is really simple. This tool is meant to be run from terminal so first open up your terminal and move to the directory of where this tool is stored. Then run python3 ShadowSharkListener.py --help to get the help or python3 ShadowSharkListener.py --lhost YOUR IP ADDRESS --lport THE PORT TO LISTEN FOR CONNECTIONS ON to start the listener. To use the payload you first need to set your IP in the place where it says IP and the port to send a connection to where it says PORT in the ShadowSharkPayload.py program. To compile the script to .exe use the ShadowSharkPayloadCompile.py program. Open the file and put the name of the icon file where it says ICON. Note the icon file and the ShadowSharkPayload.py script should both be in the same folder as the ShadowSharkPayloadCompile.py program for this to work. Now open up a terminal and go to the directory with all the files in it and run python3 ShadowSharkPayloadCompile.py py2exe. Note this compiling method can only be done by using wine or on a windows machine. To do this python 3.7 to 3.9 must be installed on wine or the windows machine. Then the command pip install py2exe should be run to install this third-party module. Now you can gain full control of any computer in which the program is run on. This program only works on Windows, MacOS, and Linux systems.
