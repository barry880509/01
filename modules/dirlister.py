# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
def run(**args):
    print "[*] in dirlister module"
    files = os.listdir(".")
    
    return str(files)