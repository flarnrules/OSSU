#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 16:56:20 2023

@author: flarnrules
"""
s = input('Please input a string: ')
max_len = 0
current = s[0]
longest = s[0]

for i in range(1, len(s)):
    # Check if the next character in s is the same or greater than the last character in current
    if s[i] >= current[-1]:
        # If so, add this character to current
        current += s[i]
        # If current is now longer than longest, replace longest with current
        if len(current) > max_len:
            max_len = len(current)
            longest = current
    else:
        # If not, reset current
        current = s[i]

print('the longest sequence is: ', longest)
