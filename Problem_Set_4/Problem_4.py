# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:00:59 2020

@author: pavk1

Problem 4 - Hand Length
0.0/10.0 points (graded)
We are now ready to begin writing the code that interacts with the player.
We'll be implementing the playHand function. This function allows the user to
play out a single hand. First, though, you'll need to implement the helper
calculateHandlen function, which can be done in under five lines of code.

"""

def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """

    count = 0
    for value in hand.values():
        count += value
    return count

# Correct
