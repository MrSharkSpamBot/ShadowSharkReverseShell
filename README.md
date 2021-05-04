# Shadow Shark Listener
A full fledged reverse TCP handler written in pure python3 that is used to interact with Shadow Shark payloads.

## Installation
### Debian
```
$ sudo apt-get install python3 git
$ git clone https://github.com/MrSharkSpamBot/Shadow-Shark-Listener.git
```
### Arch
```
$ sudo pacman -S python git
$ git clone https://github.com/MrSharkSpamBot/Shadow-Shark-Listener.git
```

## Usage
### ShadowSharkListener.py
Note: This tool is meant to be run on a Linux enviornment.
```
$ python3 ShadowSharkListener.py --help
	                                             ``
	                                       ``-+yhh-
	                                    `:ohNMMMy.                  `.-`
	                                `-ohNMMMMMM:                `.+hNy-
	             ``.-:+osyyyhhhhhdddmMMMMMMMMMm---:::--..``````+dMMMo
	      `:+syhdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNMMMMMo/-`                          ./o+
	  `+ymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMms:`                 `:ohNMd:
	`oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdo-          -+ymMMMMy-
	 :NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy/`  .+hNMMMMMNo.
	  `/+shdmymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhmMMMMMMMNo`
	  osdhdosydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo`
	  sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd/`
	   ``:shNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy/.
	       ``./ohdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdhhdmNMMMMMMNd+.
	             ``.-:/+osyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNmdhs+-`` ````.:+yhmNMMNh+.
	                       ```.-:/+syyyhhdMMMMMMMMddddddddddddhysMMMM-.`....``               ```.-/oys:
	                                     `mMMMMMMM`````````````  :hNM+
	                                      -mMMMMMM.                .+s.
	                                       .yMMMMMh`
	                                         :yNMMMh.
	                                           .odNMm:
	                                             `-/sh:
    
usage: ShadowSharkListener.py [-h] --lh LHOST --lp LPORT

This tool is a full fledged reverse TCP handler used to interact with Shadow
Shark payloads. Created by Mr. Shark Spam Bot.

optional arguments:
  -h, --help            show this help message and exit
  --lh LHOST, --lhost LHOST
                        Your IP address.
  --lp LPORT, --lport LPORT
                        The port to listen for connections on.
$ python3 ShadowSharkListener.py --lhost 0.0.0.0 --lport 8080
	                                             ``
	                                       ``-+yhh-
	                                    `:ohNMMMy.                  `.-`
	                                `-ohNMMMMMM:                `.+hNy-
	             ``.-:+osyyyhhhhhdddmMMMMMMMMMm---:::--..``````+dMMMo
	      `:+syhdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNMMMMMo/-`                          ./o+
	  `+ymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMms:`                 `:ohNMd:
	`oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdo-          -+ymMMMMy-
	 :NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy/`  .+hNMMMMMNo.
	  `/+shdmymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhmMMMMMMMNo`
	  osdhdosydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo`
	  sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd/`
	   ``:shNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy/.
	       ``./ohdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdhhdmNMMMMMMNd+.
	             ``.-:/+osyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNmdhs+-`` ````.:+yhmNMMNh+.
	                       ```.-:/+syyyhhdMMMMMMMMddddddddddddhysMMMM-.`....``               ```.-/oys:
	                                     `mMMMMMMM`````````````  :hNM+
	                                      -mMMMMMM.                .+s.
	                                       .yMMMMMh`
	                                         :yNMMMh.
	                                           .odNMm:
	                                             `-/sh:
    
[*] A reverse TCP handler on 0.0.0.0:8080 has successfully started...
```
### ShadowSharkPayload.py
This payload can run on any operating system. To configure the payload go to line
