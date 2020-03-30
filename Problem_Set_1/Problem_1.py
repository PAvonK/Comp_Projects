# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:24:08 2020

@author: PAvonK

instructions...

Assume s is a string of lower case characters

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if 
s = 'azcbobobegghakl', your program should print:

Number of vowels: 5

"""

#Enter Code Below
#s = input(str("Enter your string here: "))
s = 'azcbobobegghakl'
vowels = 0
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowels += 1
print("Numer of vowles: " + str(vowels))
