# Shadow-Shark-Listener
A full fledged reverse TCP handler used to interact with Shadow Shark payloads.

Installation:

To install this tool you need to install both any version of python from 3.7 to 3.9 and install git. On Debian, this can be done from the terminal by using the command command sudo apt-get install git python3. Other operating systems have their own ways of installing git and python3. A quick google search on how to install git and python3 for your specific operating system should tell you how to do so. To install the tool itself run the command git clone https://github.com/MrSharkSpamBot/Shadow-Shark-Listener.git in terminal.

Usage:

Note this tool is meant to be used for ethical purposes if you plan to use this for unethical purposes then do not download this tool and leave this page immediately. This tool is designed to be used on linux but should be able to work on most other operating systems. Running the tool is really simple. This tool is meant to be run from terminal so first open up your terminal and move to the directory of where this tool is stored. Then run python3 ShadowSharkListener.py --help to get the help or python3 ShadowSharkListener.py --lhost YOUR IP ADDRESS --lport THE PORT TO LISTEN FOR CONNECTIONS ON to start the listener. To use the payload you first need to set your ip in the place where it says IP and the port to send a connection to where it says PORT in the ShadowSharkPayload.py program. To compile the script to .exe use the ShadowSharkPayloadCompile.py program. Open the file and put the name of the icon file where it says ICON. Note the icon file must be in the same folder and the ShadowSharkPayload.py file must be as well. 
