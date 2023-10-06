#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:37:28 2023

@author: flarnrules
"""

def get_ratios(L1, L2):
    
    """
    Parameters
    ----------
    L1 : LIST OF NUMBERS equal length of L2.
    L2 : LIST OF NUMBERS equal lenght of L1.

    Returns
    -------
    A list containing L1[i]/L2[i], a list of ratios.
    """

    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN')) #NaN = Not a Number
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios

            