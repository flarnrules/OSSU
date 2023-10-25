#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 13:05:03 2023

@author: flarnrules
"""

def selSort(L):
    for i in range(len(L) - 1):
        print(L)
        minIndx = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp
        
test = [1, 5, 3, 8, 4, 9, 6, 2]