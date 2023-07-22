#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:22:53 2023

@author: flarnrules
"""

x = 25
epsilon = 0.1 # how close do I need to get
num_guesses = 0
low = 1.0
high = x
ans = (high + low) / 2.0

while abs(ans**2 - x) >= epsilon:
	print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
	num_guesses += 1
	if ans**2 < x:
		low = ans
	else:
		high = ans
	ans = (high + low) / 2.0
print('num_guesses = ' + str(num_guesses))
print(str(ans) + ' is close to square root of ' + str(x))