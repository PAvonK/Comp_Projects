# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:29:46 2020

@author: pavk1

instructions...

Assume s is a string of lower case characters

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2

"""
s = 'azcbobobegghakl'

count = 0
for i in range (len(s)):
    if s[i:i+3] == 'bob':
        count+=1
print("The Bob Count is: " + str(count))