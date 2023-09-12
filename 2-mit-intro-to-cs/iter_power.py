#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 11:59:48 2023

@author: flarnrules
"""
def iterPower (base, exp):
    
    result = 1
    while exp > 0:
        result = result * base
        exp -= 1
    return result

print(iterPower(2.27, 0))