# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:17:19 2020

@author: pavk1

Problem 1 - Is the Word Guessed

Please read the Hangman Introduction before starting this problem. We'll
start by writing 3 simple functions that will help us easily code the Hangman
problem. First, implement the function isWordGuessed that takes in two
parameters - a string, secretWord, and a list of letters, lettersGuessed.
This function returns a boolean - True if secretWord has been guessed (ie,
all the letters of secretWord are in lettersGuessed) and False otherwise.

Example Usage:

>>> secretWord = 'apple'
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(isWordGuessed(secretWord, lettersGuessed))
False
"""

def isWordGuessed (secretWord, lettersGuessed):
    listb = []
    for char in secretWord:
        if char in lettersGuessed:
            listb.append(char)
        elif char not in lettersGuessed:
            return False
    return True
            
print(isWordGuessed('apple', ['i', 'p', 'p', 'r', 's', 'l', 'e']))
