# -*- coding: utf-8 -*-
"""
This configuration tool generates a CadaverousCipher encryption key and writes it to dictionary_key.json.

@author: Mr. Shark Spam Bot
"""
import sys
import json
import string
import argparse
from lib.CadaverousCipher import CadaverousCipher as cc

def parse_args():
    '''Get the subdictionary_count.'''
    parser = argparse.ArgumentParser(description='''This configuration tool generates a CadaverousCipher 
encryption key and writes it to dictionary_key.json.''')
    parser.add_argument('-sdc', '--subdictionary-count', dest='subdictionary_count', required=True, type=int,
                        help='The number of sub dictionaries inside of the main dictionary which each contain unique substitutes for each character.')
    arguments = parser.parse_args()
    subdictionary_count = arguments.subdictionary_count
    return subdictionary_count

def main(subdictionary_count):
    '''Generate the dictionary key and safe it to dictionary_key.json.'''
    dictionary = cc.generate_dictionary(string.printable, subdictionary_count)
    try:
        with open('dictionary_key.json', 'w') as dictionary_key:
            json.dump(dictionary, dictionary_key)
        print('[+] Key successfully written to dictionary_key.json.\n')
        print(dictionary)
    except PermissionError:
        print('Root permissions are needed in order to write to the file dictionary_key.json.')

if __name__ == '__main__':
    sys.sys.path.append('../lib')
    main(parse_args())
