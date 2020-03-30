# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:06:01 2020

@author: pavk1
"""
shift = 4

import string

message_text = 'This is the Message Text'

lowerBaseList = string.ascii_lowercase + string.ascii_lowercase
upperBaseList = string.ascii_uppercase + string.ascii_uppercase
lowerShiftDict = {}
upperShiftDict = {}
cryptoUpperList = []
cryptoLowerList = []


for char in range(26):
    letter = upperBaseList[char]
    upperShiftDict[letter] = upperBaseList[char+shift]
#    print(upperShiftDict[letter])
for k, v in upperShiftDict.items():
    cryptoUpperList.append(v)

for char in range(26):
    letter = lowerBaseList[char]
    lowerShiftDict[letter] = lowerBaseList[char+shift]

for k, v in lowerShiftDict.items():
    cryptoLowerList.append(v)

dictKeys = lowerBaseList + upperBaseList
dictValues = cryptoLowerList + cryptoUpperList

shifted_dict = dict(zip(dictKeys, dictValues))
print(shifted_dict)

tempMessage = []
#key = shifted_dict.keys()
#value = shifted_dict.values()

for char in message_text:
    if char in shifted_dict.keys():
        letter = shifted_dict[char]
        tempMessage.append(letter)
    elif char == ' ':
        tempMessage.append(char)
        
encryptedMessage = "".join(tempMessage)

print(encryptedMessage)
    



#cryptoUpperAlphabet = "".join(cryptoUpperList)
#cryptoLowerAlphabet = "".join(cryptoLowerList)
#
#cryptoList = (cryptoUpperAlphabet + cryptoLowerAlphabet)
#print(cryptoList)







