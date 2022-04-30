# -*- coding: utf-8 -*-
"""
This script generates a CadaverousCipher encryption key and writes it to dictionary_key.json.

@author: Mr. Shark Spam Bot
"""
import string
import json
from lib import cadaverouscipher

dictionary = cadaverouscipher.generate_dictionary(string.printable)
try:
    with open('dictionary_key.json', 'w') as dictionary_key:
        json.dump(dictionary, dictionary_key)
    print('[+] Key successfully written to dictionary_key.json.')
    print(dictionary)
except PermissionError:
    print('Root permissions are needed in order to write to the file dictionary_key.json.')
