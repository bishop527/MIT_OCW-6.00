# 6.00 Problem Set 3
#
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string
from string import ascii_lowercase

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
done = False
word = choose_word(wordlist)
guesses = 8
answer = []
available = list(ascii_lowercase)
x = 0
while x < len(word):
    answer.append('_')
    x = x+1

print word

print "I am thinking of a word that is %s letters long" % len(word)
print "-------------------------------------------"

while guesses > 0 and done == False:
    print ""
    exists = False

    for x in answer:
        print x,

    print ""

    print "You have %s guesses left" % guesses

    print "Available letters: ",
    for l in available:
        print l,
    print ""

    guess = raw_input("Please guess a letter: ")

    # check that the guessed letter is still available
    if guess in available:
        available.remove(guess)
        # check if the guessed letter is in the word
        for i, e in enumerate(word):
            if guess == e:
                print "%s is in there" % guess
                answer[i] = guess
                exists = True
                if "_" not in answer:
                    print "You've guessed the word!"
                    for e in word:
                        print e,
                        done = True
        if exists == False:
            print "Sorry, %s isn't in the word" % guess
            guesses = guesses - 1
    else:
        print "You already guessed %s." % guess

if guesses == 0:
    print "Sorry, you've run out of guesses"
    print "The word was %s " % word