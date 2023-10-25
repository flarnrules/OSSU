#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 22:45:52 2023

@author: flarnrules
"""

def search(L, e):
    count = 0
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    count += 1
    return False
    print("try " + str(count) + " for newsearch")

def newsearch(L, e):
    size = len(L)
    count = 0
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
        count += 1
        print("try " + str(count) + " for newsearch")
        
    return False


test_list = [1,2,5,6]

e = 5

print("search for " + str(e) + " is " + str(search(test_list, e)))


print(newsearch(test_list, e))