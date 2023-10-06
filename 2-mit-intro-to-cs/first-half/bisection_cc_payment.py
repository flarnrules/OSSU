#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 18:07:51 2023

@author: flarnrules
"""

balance = 100
annualInterestRate = 0.20
num_guesses = 1

monthly_interest_rate = annualInterestRate/12
epsilon = 0.01
low_bound = balance / 12
high_bound = (balance *((1+monthly_interest_rate)**12))/12.0


while True:
    remaining_balance = balance
    for month in range(12):
        monthlyInterestRate = annualInterestRate / 12.0
        monthlyUnpaidBalance = remaining_balance - monthlyPayment
        remaining_balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
    if remaining_balance >= epsilon:
        low_bound = monthlyPayment
    elif:
        
        monthlyPayment = (low_bound + high_bound) / 2.0
        
    else:
        break

print("Lowest Payment: " + str(round(monthlyPayment, 2)))
