# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:06:01 2020

@author: pavk1
"""
#base = 'Wow, this is an amazing text.'
#specialCharacters = (" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
#word = base.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
#word_list = word.split()
#print('one', word_list)
##word_list = word_list_1.split()
##print('two', word_list)
word_list = ['Wow', 'this', 'is', 'an', 'amazing', 'text']

shift = 1

import string

message_text = 'Wow, this is an amazing text.'

lowerBaseList = string.ascii_lowercase + string.ascii_lowercase
upperBaseList = string.ascii_uppercase + string.ascii_uppercase

encryptingDict = {}

for char in range(26):
    letter = lowerBaseList[char]
    encryptingDict[letter] = lowerBaseList[char + shift]

for char in range(26):
    letter = upperBaseList[char]
    encryptingDict[letter] = upperBaseList[char + shift]

#print(encryptingDict)

tempMessage = []

for char in message_text:
    if char in encryptingDict.keys():
        letter = encryptingDict[char]
        tempMessage.append(letter)
    elif char not in encryptingDict.keys():
        tempMessage.append(char)

encryptedMessage = "".join(tempMessage)

print(encryptedMessage)
#encryptedMessage = 'Ewe, bpqa qa iv iuihqvo bmfb.'
#encryptedMessage = 'Wow, this is an amazing text.'

deryptingDict = {}

#newShift = 0
#print('newShift:', newShift)
#
#for char in range(26):
#    letter = lowerBaseList[char]
#    deryptingDict[letter] = lowerBaseList[char - newShift]
#
#for char in range(26):
#    letter = upperBaseList[char]
#    deryptingDict[letter] = upperBaseList[char - newShift]

bestShiftValue = 0

#print(numValidWords)

#testString = []
newShift = 0

while bestShiftValue != newShift:
#    newShift = 0
    
    for char in range(26):
        letter = lowerBaseList[char]
        deryptingDict[letter] = lowerBaseList[char - newShift]

    for char in range(26):
        letter = upperBaseList[char]
        deryptingDict[letter] = upperBaseList[char - newShift]
    
    bestShiftValue = 0
    numValidWords = 0
    notValidCount = 0
    decryptingMessage = ''
    testString = []
    
    for char in encryptedMessage:
        if char in deryptingDict.keys():
            letter = deryptingDict[char]
            testString.append(letter)
        elif char == ' ':
            testString.append(char)

    decryptingMessage = "".join(testString)

    message = decryptingMessage.split()
    #print(message)
    #print('end')

    for word in message:
        if word in word_list:
            numValidWords += 1

        elif word not in word_list:
            notValidCount += 1

    print('valid: ', numValidWords)
    print('not valid: ', notValidCount)

    if numValidWords != len(message):
        newShift += 1
        print(newShift)
    elif best
        bestShiftValue = newShift
        break

#    print('eureka')
    
    print('Best Shift Value:', bestShiftValue)

    print('afterShift:', newShift)


