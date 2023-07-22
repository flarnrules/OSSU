#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 16:32:45 2023

@author: flarnrules
"""

count = 0
s = input('input a string: ')
for letters in s:
    if letters == 'a' or letters == 'e' or letters == 'i' or letters == 'o' or letters == 'u':
        count += 1
    else:
        continue

print('Number of vowels: ', count)