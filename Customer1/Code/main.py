import sys
import os

# Add the library folder to the sys.path to import lib.py
sys.path.append(os.path.join(os.path.dirname(__file__), '../library'))

from lib import shared_util

print("Hello from folder1!")
shared_util()
