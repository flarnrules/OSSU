#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 13:06:07 2023

@author: flarnrules
"""

def isPal(x):
    assert type(x) == list
    temp = x[:]
    print('before reverse', temp, x)
    temp.reverse()
    print('after reverse', temp, x)
    if temp == x:
        return True
    else:
        return False
    
def silly(n):
    result = []
    for i in range(n):
        
        elem = input('Enter element: ')
        result.append(elem)
    
    if isPal(result):
        print('Yes')
    else:
        print('No')
        
