# -*- coding: utf-8 -*-
"""
An uncrackable substitution cipher using randomly generated characters.

@author: Mr. Shark Spam Bot
"""
import random

def generate_dictionary(characters):
    '''
    Generate a dictionary which serves as an encryption key.

    Parameters
    ----------
    characters : str
        Characters to each be paired with a unique substitute.

    Returns
    -------
    dictionary : dict
        The encryption / decryption key.

    '''
    if not isinstance(characters, str):
        raise TypeError('characters must be a str object')
    dictionary = {}
    for character in characters:
        substitute_character = chr(random.randint(0, 1000000))
        while True:
            if not substitute_character in dictionary.values():
                break
            substitute_character = chr(random.randint(0, 1000000))
        dictionary.update({character: substitute_character})
    return dictionary

def encrypt(text, dictionary):
    '''
    Encrypt text using the dictionary as an encryption key.

    Parameters
    ----------
    text : str
        The text to encrypt.
    dictionary : dict
        The encryption key.

    Returns
    -------
    encrypted_text : str
        The encrypted text.

    '''
    if not isinstance(text, str):
        raise TypeError('text must be a str object')
    if not isinstance(dictionary, dict):
        raise TypeError('dictionary must be a dict object')
    encrypted_text = ''
    for character in text:
        if character in dictionary.keys():
            encrypted_text += dictionary[character]
        else:
            encrypted_text += character
    return encrypted_text

def decrypt(text, dictionary):
    '''
    Decrypt text using the dictionary as a dectyption key.

    Parameters
    ----------
    text : str
        The text to decrypt.
    dictionary : dict
        The decryption key.

    Returns
    -------
    decrypted_text : str
        The decrypted text.

    '''
    if not isinstance(text, str):
        raise TypeError('text must be a str object')
    if not isinstance(dictionary, dict):
        raise TypeError('dictionary must be a dict object')
    decrypted_text = ''
    characters = list(dictionary.keys())
    substitute_characters = list(dictionary.values())
    for substitute_character in text:
        if substitute_character in substitute_characters:
            decrypted_text += characters[substitute_characters.index(substitute_character)]
        else:
            decrypted_text += substitute_character
    return decrypted_text
