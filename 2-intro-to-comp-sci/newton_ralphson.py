#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 16:14:57 2023

@author: flarnrules
"""

epsilon = 0.01 #how close we wanna be
y = 54.0 #what are we tryin to get
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y)>= epsilon:
	numGuesses += 1
	guess = guess - (((guess**2) - y) / (2*guess))
print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))