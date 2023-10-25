#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:57:08 2023

@author: flarnrules
"""
from sortedcontainers import SortedList
import random

def bogo_sort(L):
    
    sorted_L = SortedList(L)
    count = 0
    
    while sorted_L != L:    
        random.shuffle(L)
        sorted_L = SortedList(L)
        print(L)
        count += 1
    print (count)
    return L

L = [5, 4, 9, 10]
