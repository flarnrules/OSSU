#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 16:18:49 2023

@author: flarnrules
"""

# print longest substring in alphabetical order

s = 'carhotdogmrtacoman'

current_substring = s[0]
longest_substring = s[0]

for char in range(1, len(s)):
    if s[char] >= s[char - 1]:
        current_substring += s[char]
    else:
        current_substring = s[char]
    
    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

print ("Longest substring in alphabetical order is: " + str(longest_substring))