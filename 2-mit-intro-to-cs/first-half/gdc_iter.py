#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 17:08:13 2023

@author: flarnrules
"""
'''

a, b: positive integers

returns: a positive integer, the greatest common divisor of a & b

'''


def gcdIter(a, b):
    
    # test value = to smaller of two inputs
   
    if a < b:
        test = a
    else:
        test = b

    # decrease test by 1 every time the remainder of both is not 0
    while test > 0:
        if a%test == 0 and b%test == 0:
            return test
        else:
            test -= 1
            

print(gcdIter(300, 456))

    
    
    
    
        
    