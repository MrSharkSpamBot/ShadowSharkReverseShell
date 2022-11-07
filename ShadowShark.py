#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The multipurpose tool to use all ShadowSharkReverseShell features.

@author: Mr. Shark Spam Bot
"""

import readline
from lib.common import parser
from lib.server import listener

def main() -> None:
    lhost, lport, encryption, dictionary_key, key = parser.get_arguments()
    listener.ShadowShark(lhost, lport, encryption, dictionary_key, key).main()

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
