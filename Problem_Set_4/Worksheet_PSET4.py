# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 14:45:51 2020

@author: pavk1
"""

list = []
dict1 = {'a':1, 'b':2, 'c':0}

for key in dict1.keys():
    list.append(key)
str1 = ' '.join(list)
print(str1)  

print()
print()

tempDict = {}
for k, v in dict1.items():
    if v > 0:
        tempDict.update({k:v})

print(tempDict)
        