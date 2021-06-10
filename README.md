# Shadow Shark Listener
A full fledged reverse TCP handler written in pure python3 that is used to interact with Shadow Shark payloads.

## Installation
### Debian
```
$ sudo apt-get install python3 git
$ git clone https://github.com/MrSharkSpamBot/ShadowSharkListener.git
```
### Arch
```
$ sudo pacman -S python git
$ git clone https://github.com/MrSharkSpamBot/ShadowSharkListener.git
```

## Usage
### ShadowSharkListener.py
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
                     ``.-:/+osyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdhs+-`` ````.:+yhmNMMNh+.
                               ```.-:/+syyyhhdMMMMMMMMddddddddddddddNMMMMdo/:...``               ```.-/oys:
                                             `mMMMMMMM``````````````.sNMMh
                                              -mMMMMMM.               .smMy`
                                               .yMMMMMh`                `:ys.
                                                 :yNMMMh.
                                                   .odNMm:
                                                     `-/sh:

usage: ShadowSharkListener.py [-h] --lh LHOST --lp LPORT --encryption
                              ENCRYPTION

This tool is a full fledged reverse TCP handler used to interact with Shadow
Shark payloads. Created by Mr. Shark Spam Bot.

optional arguments:
  -h, --help            show this help message and exit
  --lh LHOST, --lhost LHOST
                        Your IP address.
  --lp LPORT, --lport LPORT
                        The port to listen for connections on.
  --encryption ENCRYPTION, -e ENCRYPTION
                        The encryption used for sent and recieved data.
$ python3 ShadowSharkListener.py --lhost 0.0.0.0 --lport 8080 --encryption hex
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
This payload can run on any operating system. To configure the payload go to line 29 and replace IP with your IP and replace PORT with the port on your computer you want connections be sent to and from.
### ShadowSharkPayloadCompile.py
This compilation script can only be run on a windows machine or by using wine. To configure the compilation script go to line 14 and replace ICON with the icon file you want your exe file to have to have. To do this make sure that the ShadowSharkPayload.py script, your icon file, and the ShadowSharkPayloadCompile.py script are in the same folder and that py2exe is installed.
```
# First install python3 on your windows machine or wine environment.
$ pip install py2exe
$ python ShadowSharkPayloadCompile.py py2exe
```
