#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 23:08:43 2023

@author: flarnrules
"""

print("Please think of a number between 0 and 100!")

guess = 50
response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")



while response != 'c':

    print("Is your secret number " + str(guess) + "?")

    input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if response == 'l':
        guess = guess * 2
    elif response == 'h':
        guess = guess / 2
    else:
        print("Sorry, I did not understand your input.")

print("Game over. Your secret number was: " + str(guess))
