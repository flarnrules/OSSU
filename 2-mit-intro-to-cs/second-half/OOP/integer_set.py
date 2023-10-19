#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:53:48 2023

@author: flarnrules
"""

class IntSet(object):
    def __init__(self):
        self.vals = []
    
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
    
    def member(self, e):
        return e in self.vals
    
    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'
    
    def intersect(self, other_set):
        intersection = IntSet()
        
        for e in self.vals:
            if other_set.member(e):
                intersection.insert(e)
        
        return intersection
    
    def __len__(self):
        return len(self.vals)
    
