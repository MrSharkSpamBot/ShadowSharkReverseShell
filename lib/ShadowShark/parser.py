# -*- coding: utf-8 -*-
"""
The argument parser for the Shadow Shark listener.

@author: Mr. Shark Spam Bot
"""
import json
import socket
import argparse

def get_arguments():
    '''Get the lhost, lport, encryption, and dictionary_key.'''
    parser = argparse.ArgumentParser(description='''This tool is a full fledged reverse TCP handler
used to interact with Shadow Shark payloads. Created by Mr. Shark Spam Bot.''')
    parser.add_argument('-lh', '--lhost', dest='lhost', required=True, type=str,
                        help='Your IP address.')
    parser.add_argument('-lp', '--lport', dest='lport', required=True, type=int,
                        help='The port to listen for connections on.')
    parser.add_argument('-e', '--encryption', dest='encryption', required=True,
                        type=str, help='The encryption used for sent and recieved data.')
    arguments = parser.parse_args()
    lhost = arguments.lhost
    lport = arguments.lport
    encryption = arguments.encryption.lower()
    dictionary_key = {}
    try:
        socket.inet_aton(lhost)
    except socket.error:
        parser.error('Invalid value specified for LHOST.')
    if lhost.count('.') != 3:
        parser.error('Invalid value specified for LHOST.')
    if encryption not in ['hex', 'base64', 'cadaverouscipher']:
        parser.error('Only hex, base64, and CadaverousCipher encryptions are supported.')
    if encryption == 'cadaverouscipher':
        try:
            with open('Configuration/dictionary_key.json', 'r') as dictionary_key:
                dictionary_key = json.load(dictionary_key)
        except FileNotFoundError:
            parser.error('The file dictionary_key.json does not exist in the ShadowSharkReverseShell directory.')
        except PermissionError:
            parser.error('Root permissions are needed in order to read the file dictionary_key.json.')
        except json.decoder.JSONDecodeError:
            parser.error('Invalid key found in dictionary_key.json.')
    return [lhost, lport, encryption, dictionary_key]
