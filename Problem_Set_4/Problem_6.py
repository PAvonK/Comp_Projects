# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:03:57 2020

@author: pavk1

Problem 6 - Playing a Game

A game consists of playing multiple hands. We need to implement one final
function to complete our word-game program. Write the code that implements the
playGame function. You should remove the code that is currently uncommented in
the playGame body. Read through the specification and make sure you understand
what this function accomplishes. For the game, you should use the HAND_SIZE
constant to determine the number of cards in a hand.

Testing: Try out this implementation as if you were playing the game. Try out
different values for HAND_SIZE with your program, and be sure that you can
play the wordgame with different hand sizes by modifying only the variable
HAND_SIZE.

Sample Output
Here is how the game output should look...
Hints about the output
Entering Your Code
A Cool Trick about 'print'


"""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1
    """

    storedHand = 'placeHolder'
    n = HAND_SIZE
    while True:
        userInput = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")

        if userInput is 'n':
            hand = dealHand(n)
            storedHand = hand
            playHand(hand, wordList, n)

        elif userInput is 'r':
            if storedHand == 'placeHolder':
                print("You have not played a hand yet. Please play a new hand first!")
            else:
                playHand(storedHand, wordList, n)
                #break

        elif userInput is 'e':
            break

        else:
            print("Invalid command")

# correct
