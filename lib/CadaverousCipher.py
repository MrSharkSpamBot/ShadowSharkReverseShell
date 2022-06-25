# -*- coding: utf-8 -*-
"""
A permutation based substitution cipher which uses randomly generated characters as substitutes.

@author: Mr. Shark Spam Bot
"""
import secrets
import itertools

def generate_dictionary(characters, subdictionary_count):
    '''
    Generate a dictionary which serves as an encryption key.

    Parameters
    ----------
    characters : str
        Characters to each be paired with one or more unique substitutes.
    subdictionary_count : int
        The number of sub dictionaries inside of the main dictionary which each contain unique substitutes for each character.

    Returns
    -------
    dictionary : dict
        The encryption / decryption key.

    '''
    if not isinstance(characters, str):
        raise TypeError('characters must be a str object')
    if not isinstance(subdictionary_count, int):
        raise TypeError('dictionary_count must be an int object')
    dictionary = {}
    system_random = secrets.SystemRandom()
    for i in range(1, (subdictionary_count + 1)):
        sub_dictionary = {}
        for character in characters:
            substitute_character = chr(system_random.randint(0, 1000000))
            while True:
                if not substitute_character in sub_dictionary.values():
                    break
                substitute_character = chr(system_random.randint(0, 1000000))
            sub_dictionary.update({character: substitute_character})
        dictionary.update({i: sub_dictionary})
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
    len_dictionary_keys = len(dictionary.keys())
    perms = list(itertools.permutations(range(1, len_dictionary_keys+1)))
    sliced_text = []
    for i in range(0, len(text), len_dictionary_keys):
        sliced_text.append(text[i: i+len_dictionary_keys])
    index = 0
    for slice_chars in sliced_text:
        if index >= len(perms):
            index = 0
        perm = perms[index]
        for number, character in itertools.zip_longest(perm, slice_chars):
            if not character:
                break
            if character in dictionary[number].keys():
                encrypted_text += dictionary[number][character]
            else:
                encrypted_text += character
        index += 1
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
    len_dictionary_keys = len(dictionary.keys())
    perms = list(itertools.permutations(range(1, len_dictionary_keys+1)))
    sliced_text = []
    for i in range(0, len(text), len_dictionary_keys):
        sliced_text.append(text[i: i+len_dictionary_keys])
    index = 0
    for slice_chars in sliced_text:
        if index >= len(perms):
            index = 0
        perm = perms[index]
        for number, substitute_character in itertools.zip_longest(perm, slice_chars):
            if not substitute_character:
                break
            characters = list(dictionary[number].keys())
            substitute_characters = list(dictionary[number].values())
            if substitute_character in substitute_characters:
                decrypted_text += characters[substitute_characters.index(substitute_character)]
            else:
                decrypted_text += substitute_character
        index += 1
    return decrypted_text
