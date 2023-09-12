#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:23:31 2023

@author: flarnrules
"""

def recur_power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * recur_power(base, exp-1)

print(recur_power(5, 0))