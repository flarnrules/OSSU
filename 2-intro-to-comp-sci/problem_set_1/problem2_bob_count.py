#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 16:44:40 2023

@author: flarnrules
"""

bob_count = 0
s = input('please input a string: ')
for bobs in range(len(str(s))-2):
    if s[bobs:bobs+3] == 'bob':
        bob_count += 1

print('Number of times bob occurs is: ', bob_count)
