# -*- coding: utf-8 -*-
"""
A polyalphabetic substitution cipher which uses randomly generated characters as substitutes.

@author: Mr. Shark Spam Bot
"""
import secrets

def generate_dictionary(characters):
    '''
    Generate a dictionary which serves as an encryption key.

    Parameters
    ----------
    characters : str
        Characters to each be paired with two unique substitutes.

    Returns
    -------
    dictionary : dict
        The encryption / decryption key.

    '''
    if not isinstance(characters, str):
        raise TypeError('characters must be a str object')
    dictionary = {}
    system_random = secrets.SystemRandom()
    for i in range(1, 3):
        half_dictionary = {}
        for character in characters:
            substitute_character = chr(system_random.randint(0, 1000000))
            while True:
                if not substitute_character in half_dictionary.values():
                    break
                substitute_character = chr(system_random.randint(0, 1000000))
            half_dictionary.update({character: substitute_character})
        dictionary.update({i: half_dictionary})
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
    dictionary1 = dictionary[1]
    dictionary2 = dictionary[2]
    for index, character in enumerate(text):
        if character in dictionary1.keys() or character in dictionary2.keys():
            if index % 2 == 0:
                encrypted_text += dictionary2[character]
            else:
                encrypted_text += dictionary1[character]
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
    dictionary1 = dictionary[1]
    dictionary2 = dictionary[2]
    characters1 = list(dictionary1.keys())
    substitute_characters1 = list(dictionary1.values())
    characters2 = list(dictionary2.keys())
    substitute_characters2 = list(dictionary2.values())
    for index, substitute_character in enumerate(text):
        if substitute_character in substitute_characters1 or substitute_character in substitute_characters2:
            if index % 2 == 0:
                decrypted_text += characters2[substitute_characters2.index(substitute_character)]
            else:
                decrypted_text += characters1[substitute_characters1.index(substitute_character)]
        else:
            decrypted_text += substitute_character
    return decrypted_text
