#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:49:12 2023

@author: flarnrules
"""

def bubble_sort(L):
    swap = False
    count = 0
    while not swap:
   
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
                count += 1
                print(L)
    print("sort required " + str(count) + " attempts")            
    return L
                

L = [5, 9, 15, 20, 12, 4, 2, 1, 9]

