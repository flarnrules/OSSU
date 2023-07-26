#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 10:49:48 2023

@author: flarnrules
"""

low = 0
high = 100
guess = int((low + high) / 2)

print ("Please think of a number between 0 and 100! ")


while True:
    response = None
    print ("Is your secret number " + str(guess) + "?")
    response = input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate that the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    while response not in ['h', 'c', 'l']:
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(guess) + "?")
        response = input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate that the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if response == 'c':
        break
    
    if response == 'l':
        low = guess
    
    else:
        high = guess
    
    guess = int((low + high) / 2)
    
print ('Game over. Your secret number was: ', guess)
    
    