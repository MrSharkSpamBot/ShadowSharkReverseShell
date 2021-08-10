# -*- coding: utf-8 -*-
"""
This script is used to compile Shadow Shark payloads into stand alone exe files.

@author: Mr. Shark Spam Bot
"""
import distutils
import sys
import py2exe

sys.argv.append('py2exe')
distutils.core.setup(
    options = {'py2exe': {'bundle_files': 1, 'excludes': ['tkinter'], 'compressed': True}},
    windows = [{'script': 'ShadowSharkPayload.py', 'icon_resources': [(1, 'ICON')]}], # Set icon on this line.
    zipfile = None,
)
