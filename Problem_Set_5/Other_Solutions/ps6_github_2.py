'''
This code will apply and decrypt a Caesar Cypher - messages where every letter has been shifted
down the alphabet by a number of letters.
E.g. a shift of 3 would turn "b" into "e", and "f" into "i".
Un-encrypting involves trying every letter shift and checking the result against a
list of valid English words (this could also be feasibly accomplished manually, as - assuming
every letter is shifted by the same amount - there will only be 25 possibilities.

This is an original answer to Problem Set 6 of edX MITx: 6.00.1x
Introduction to Computer Science and Programming Using Python, Spring 2016

Some comments have been left in as learning reminders.
'''

import string
#import string.punctuation as pnct !!RAISES "ImportError: No module named punctuation"
#import string.digits as dgts
#import string.ascii_lowercase as lwcs
#import string.ascii_uppercase as upcs

WORDLIST_FILENAME = 'words.txt'

def load_words(WORDLIST_FILENAME):

    with open(WORDLIST_FILENAME, 'r') as words:

        wordLine = words.readline()

        wordList = wordLine.split()

        return wordList


def is_word(valid_words, word):

    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")

    return word in valid_words


def get_story_string(ENCRYPTED_FILENAME):

    with open(ENCRYPTED_FILENAME, "r") as encrypted:

        story = str(encrypted.read())

    return story


class Message(object):

    def __init__(self, text):

        '''
        text (str): the message's text

        a Message object has two attributes:
            self.message_text (str, determined by input text)
            self.valid_words (list, determined using function load_words)
        '''

        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    '''
    These comments are for an implementation using setters & getters instead
    of accessing properties directly, which is bad practice in Python.
    http://archive.is/TJekr
    '''

    #def get_message_text(self):
        #Used to safely access self.message_text outside of the class
        #return self.message_text
    #def get_valid_words(self):
        #Used to safely access a copy of self.valid_words outside of the class
        #Returns: a COPY of self.valid_words
        #return self.valid_words[:]


    def build_shift_dict(self, shift):

        '''
        Creates a dict that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys each of all the uppercase letters and all the lowercase
        letters.

        shift (int): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns a dictionary mapping each letter to another (shifted) letter.
        '''

        shift_dict = {}
        lowercases = string.ascii_lowercase + string.ascii_lowercase
        UPPERCASES = string.ascii_uppercase + string.ascii_uppercase

        for i, letter in enumerate(lowercases[:26]):

            shift_dict[letter] = lowercases[i + shift]

        for i, LETTER in enumerate(UPPERCASES[:26]):

            shift_dict[LETTER] = UPPERCASES[i + shift]

        return shift_dict


    def apply_shift(self, shift):

        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (int): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''

        shift_dict = self.build_shift_dict(shift)
        textCopy = self.message_text[:]
        newText = []

        for i in range(len(textCopy)):

            if textCopy[i] in string.ascii_lowercase or string.ascii_uppercase and textCopy[i] != ' ' and textCopy[i] not in string.digits and textCopy[i] not in string.punctuation:

                newText.append(shift_dict[textCopy[i]])

            elif textCopy[i] == ' ':

                newText.append(' ')

            else:

                newText.append(textCopy[i])

        newText = ''.join(newText)

        return newText


class PlaintextMessage(Message):

    def __init__(self, text, shift):

        '''
        Initializes a PlaintextMessage object

        text (str): the message's text
        shift (int): the shift associated with this message

        A PlaintextMessage object inherits from Message and has three other attributes:

            self.shift (int, determined by input shift)
            self.encrypting_dict (dict, built using shift)
            self.message_text_encrypted (str, created using shift)
        '''

        Message.__init__(self, text)

        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, self.shift)
        self.message_text_encrypted = Message.apply_shift(self, self.shift)


    #def get_shift(self):
        #Used to safely access self.shift outside of the class
        #return self.shift
    #def get_encrypting_dict(self):
        #Used to safely access a copy self.encrypting_dict outside of the class
        #import copy
        #return copy.deepcopy(self.encrypting_dict)
    #def get_message_text_encrypted(self):
        #Used to safely access self.message_text_encrypted outside of the class
        #return self.message_text_encrypted


    def change_shift(self, shift):

        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift (ie. self.encrypting_dict and
        message_text_encrypted).

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26
        '''

        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, self.shift)
        self.message_text_encrypted = Message.apply_shift(self, self.shift)


class CiphertextMessage(Message):

    def __init__(self, text):

        '''
        Initializes a CiphertextMessage object

        text (str): the message's text
        '''

        Message.__init__(self, text)


    def decrypt_message(self):

        '''
        Decrypt self.message_text by trying every possible shift value
        and finding the "best" one - the shift that
        creates the maximum number of real words. If s is the original shift value
        used to encrypt the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: there may be multiple "best" translations.

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''

        bestCount = 0
        bestTryShift = 0

        for tryshift in range(0, 26):

            count = 0
            newText = self.apply_shift(26-tryshift)
            newText = newText.split()

            for word in newText:

                if is_word(self.valid_words, word):

                    count += 1

            if count > bestCount:

                bestCount = count
                bestTryShift = tryshift

            if bestTryShift == 0:

                bestTryShift = 26

        return (bestTryShift, Message.apply_shift(self, 26-bestTryShift))

# KEY FUNCTIONS #

def decrypt_story(text):

    if '.txt' in text:

        Cipher = CiphertextMessage(get_story_string(text))

    else:

        Cipher = CiphertextMessage(text)

    return Cipher.decrypt_message()

def encrypt_story(text, shift):

    Plaintext = PlaintextMessage(text, shift)

    return Plaintext.apply_shift(shift)

# EXAMPLES #

print('Decrypting a .txt file: ', decrypt_story('story.txt'))
print('\n')
to_encrypt = 'Happy families are all alike; every unhappy family is unhappy in its own way.'
print('Example plaintext message: ', '\"', to_encrypt, '\"')
print('\n')
encrypted_example = encrypt_story(to_encrypt, 3)
print('The example, now encrypted with a shift of 3: ', encrypted_example)
print('\n')
print('The example, once again in decrypted form: ', decrypt_story(encrypted_example))
