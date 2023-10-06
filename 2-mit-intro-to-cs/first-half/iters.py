#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 09:30:03 2023

@author: flarnrules
"""

x = 3
ans = 0
itersLeft = x
while (itersLeft != 0) :
	ans = ans + x
	itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + '=' + str(ans))