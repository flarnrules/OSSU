#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 22:58:46 2023

@author: flarnrules
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    newTup = ()
    for index in range(0, len(aTup), 2):
        newTup = newTup + (aTup[index],)
    return newTup

aTup = (1, 2, 3, 4)
print(oddTuples(aTup))