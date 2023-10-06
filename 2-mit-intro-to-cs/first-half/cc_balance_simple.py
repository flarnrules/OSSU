#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 23:45:08 2023

@author: flarnrules
"""

months = 12
month_count = 0

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


for month in range(months):
    month_count += 1
    monthly_payment = balance * monthlyPaymentRate
    balance = balance - monthly_payment
    monthly_interest = balance * (annualInterestRate / 12)
    balance = balance + monthly_interest
    print("month 1 balance " + str(round(balance, 2)))
    

print(round(balance,2))