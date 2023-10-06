#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 00:43:50 2023

@author: flarnrules
"""


print("Please think of a number between 0 and 100!")

high_range = 100
low_range = 0
guess = int((high_range + low_range) / 2)
print("Is your secret number " + str(guess) + "?")
response = 0


while response != 'c':
    
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if response == 'l':
        low_range = guess
        guess = int((high_range + low_range) / 2)
        print("Is your secret number " + str(guess) + "?")
    elif response == 'h':
        high_range = guess
        guess = int((high_range + low_range) / 2)
        print("Is your secret number " + str(guess) + "?")
    elif response == 'c':
        print("Game over. Your secret number was: " + str(guess))
    else:
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(guess) + "?")

        
# if guess is too high, like 75. the previous guess becomes the low range

# if guess is too low, like 35. the previous guess becomes the  high range.
        
    
