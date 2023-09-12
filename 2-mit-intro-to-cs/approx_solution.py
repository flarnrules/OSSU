#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 08:19:45 2023

@author: flarnrules
"""

cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.01
num_guesses = 0

while abs (guess**3 - cube) >= epsilon:
	guess += increment
	num_guesses += 1
print("num_guesses =", num_guesses)
if abs (guess**3 - cube) >= epsilon:
	print("Failed on cube root of ", cube)
else:
	print(guess, 'is close to the cube root of', cube)