wordList = ['list', 'evil', 'nope', 'tow', 'fast']
hand = {'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}
n = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """

    subScore = 0
    for letter in word:
        for value in letter:
            value = SCRABBLE_LETTER_VALUES[letter]
            letterScore = value
        subScore += letterScore
    sumScore = subScore * len(word)
    if len(word) == n:
        score = sumScore + 50
    else:
        score = sumScore
    return score

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """

    remainingHand = hand.copy()
    for letter in word:
        if letter in remainingHand.keys():
            remainingHand[letter] = remainingHand.get(letter, 0) -1
    return remainingHand

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """

    if word not in wordList:
        return False
    else:
        workingHand = hand.copy()
        for letter in word:
            if letter not in workingHand.keys():
                return False
            elif letter in workingHand.keys():
                if workingHand.get(letter, 0) <= 0:
                    return False
                workingHand[letter] = workingHand.get(letter, 0) -1
        return True

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

playHand(hand, wordList, n)
    
    




