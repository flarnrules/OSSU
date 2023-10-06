#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 18:00:33 2023

@author: flarnrules
"""

def gdcRecur (a, b):
    if b == 0:
        return a
    else:
        return gdcRecur (b, a %b)

print(gdcRecur(12345678, 12))