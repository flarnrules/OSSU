#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 17:31:24 2023

@author: flarnrules
"""

ans = 0
neg_flag = False
x = int(input("enter an integer: "))
if x < 0:
	neg_flag = True
while ans**2 < x:
	ans = ans + 1
if ans**2 == x:
	print("Square root of", x, "is", ans)
else:
	print(x,"is not a perfect square")
	if neg_flag:
		print("Just checking... did you mean", -x, "?")