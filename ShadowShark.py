# -*- coding: utf-8 -*-
"""
This tool is a full fledged reverse TCP handler used to interact with Shadow Shark payloads.

@author: Mr. Shark Spam Bot
"""
import readline
import lib.ShadowShark.parser
import lib.ShadowShark.listener

def main():
    lhost, lport, encryption, dictionary_key = parser.get_arguments()
    listener.ShadowShark(lhost, lport, encryption, dictionary_key).main()

if __name__ == '__main__':
    print('''
\t                                             ``
\t                                       ``-+yhh-
\t                                    `:ohNMMMy.                  `.-`
\t                                `-ohNMMMMMM:                `.+hNy-
\t             ``.-:+osyyyhhhhhdddmMMMMMMMMMm---:::--..``````+dMMMo
\t      `:+syhdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNMMMMMo/-`                          ./o+
\t  `+ymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMms:`                 `:ohNMd:
\t`oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdo-          -+ymMMMMy-
\t :NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy/`  .+hNMMMMMNo.
\t  `/+shdmymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhmMMMMMMMNo`
\t  osdhdosydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo`
\t  sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd/`
\t   ``:shNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy/.
\t       ``./ohdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdhhdmNMMMMMMNd+.
\t             ``.-:/+osyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdhs+-`` ````.:+yhmNMMNh+.
\t                       ```.-:/+syyyhhdMMMMMMMMddddddddddddddNMMMMdo/:...``               ```.-/oys:
\t                                     `mMMMMMMM``````````````.sNMMh
\t                                      -mMMMMMM.               .smMy`
\t                                       .yMMMMMh`                `:ys.
\t                                         :yNMMMh.
\t                                           .odNMm:
\t                                             `-/sh:
    ''')
    main()
