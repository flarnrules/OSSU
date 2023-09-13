#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 23:01:31 2023

@author: flarnrules
"""

# end of year one credit card balance
# int rate / 12 = monthly int rate
# steps:
    # make payment ~ balance * payment rate
    # accrue interest ~ new balance * monthly int rate
    # calculate next beginning balance ~ new balance + interest
    # repeat

def credit_card_balance (balance, annual_int_rate, monthly_pmt_rate):
    '''

    Parameters
    ----------
    balance : float or int
        the credit card balance at month 0.
    
    annual_int_rate : float as decimal
        the annual interest rate expressed as a decimal
    
    monthly_pmt_rate : float as decimal
        the required monthly payment percentage

    Returns
    -------
    remaining balance at the end of 12 months

    '''
    months = 12
    monthly_int_rate = annual_int_rate / months
    payment = balance * monthly_pmt_rate
    new_balance = balance - payment
    monthly_interest = new_balance * monthly_int_rate
    month_count = 0
    
    for month in range(months):
        month_count += 1
        balance -= payment
        balance += monthly_interest
        print("Month " + str(month_count) + " Ending balance: $" + str(round(balance, 2)))
    
    return "The balance after 12 months is $" + str(round(balance, 2))
        

print(credit_card_balance ( 42, 0.2, 0.04 ))
        
        