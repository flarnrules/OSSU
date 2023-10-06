#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 19:43:11 2023

@author: flarnrules
"""

try:
    a = int(input("Tell me one number:"))
    b = int(input("Tell me another number:"))
    print(a/b)
    print("Okay")
except:
    print("Bug in user input.")
print("Outside")
