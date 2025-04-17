import sys
import os

# Add library folder to Python path
sys.path.append(os.path.abspath('../library'))

from lib import shared_util

print("Hello from folder1!")
shared_util()
