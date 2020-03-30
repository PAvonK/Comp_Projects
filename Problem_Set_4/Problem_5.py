# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:05:27 2020

@author: pavk1

Problem 5 - Playing a Hand

In ps4a.py, note that in the function playHand, there is a bunch of pseudocode.
This pseudocode is provided to help guide you in writing your function. Check
out the Why Pseudocode? resource to learn more about the What and Why of Pseudocode
before you start coding your solution.

Note: Do not assume that there will always be 7 letters in a hand! The
parameter n represents the size of the hand.

Testing: Before testing your code in the answer box, try out your
implementation as if you were playing the game. Here is some example output
of playHand:

"""

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    score = 0
    while len(hand.values()) > 0:
        startList = []
        str1 = []
        
        if calculateHandlen(hand) > 0:
            for key in hand.keys():
                startList.append(key)
            str1 = ' '.join(startList)
            print(str1)
            word = input('Enter word, or a "." to indicate that you are finished:')
            
            if word == ".":
                print('Your Game is over, your score is:', score)
                break
            else:
                if isValidWord(word, hand, wordList) is False:
                    print("Invalid word, please try again.")
                    print()
                else:
                    currentScore = getWordScore(word, n)
                    score += currentScore
                    print("'"+word+"'", "earned", currentScore, "points. Total:", score, "points")
                    print()
                    hand = updateHand(hand,word)
                    tempDict = {}
                    for k, v in hand.items():
                        if v > 0:
                            tempDict.update({k:v})
                    hand.clear()
                    hand = tempDict

    if len(hand.values()) == 0:
        print("Run out of letters. Total score:", score, "points.")

# Correct