"""
find_out_where_python_is_installed.py
@author: Jackie Johnson-Dallas
Created January 23, 2025
This script print the location where python is installed.
"""

import sys

locate_python = sys.exec_prefix

print(f"Python is installed at: ${locate_python}")
