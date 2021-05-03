import distutils
import sys
import py2exe

sys.argv.append("py2exe")
distutils.core.setup(
    options = {'py2exe': {'bundle_files': 1, 'excludes': ['tkinter'], 'compressed': True}},
    windows = [{'script': "payload.py", "icon_resources": [(1, "setup1.ico")]}], 
    zipfile = None,
)
