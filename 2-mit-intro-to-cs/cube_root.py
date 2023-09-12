#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 15:24:36 2023

@author: flarnrules
"""

cube = 8

for guess in range(abs(cube+1)): # i don't undertand cube +1... is it because we have 0, 1, 2, 3, 4, 5, 6, 7? and we need 8?
    if guess**3 >= abs(cube):
        break
    
if guess**3 != abs(cube):
    print(cube, ' is not a perfect cube')

else:
    if cube < 0:
        guess = -guess
    
    print("Cube root of " + str(cube) + " is ", str(guess))