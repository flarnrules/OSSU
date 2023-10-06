#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:49:23 2023

@author: flarnrules
"""

def get_stats(class_list):
	new_stats = []
	for elt in class_list:
		new_stats.append([elt[0], elt[1], avg(elt[1])])
	return new_stats

def avg(grades):
	return sum(grades)/len(grades)

test_grades = [[['peter','parker'], [80.0, 70.0, 85.0]],
			  [['bruce', 'wayne'], [100.0, 80.0, 74.0]]]
