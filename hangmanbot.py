"""
Functions for playing hangman.
words.txt and docstrings taken from MIT OCW 600.1 aside from minor changes in
order to work with platforms outside of terminal
"""

import random
import string

WORDLIST_FILENAME = "words.txt"

class HangMan():

    def __init__(self):
        self.load_words()
        self.letters_guessed = []

    def load_words(self):
        """
        Returns a list of valid words. Words are strings of lowercase letters.
        
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print("Loading word list from file...")
        # inFile: file
        inFile = open(WORDLIST_FILENAME, 'r')
        # line: string
        line = inFile.readline()
        # wordlist: list of strings
        wordlist = line.split()
        print("  ", len(wordlist), "words loaded.")
        self.wordlist = wordlist

    def choose_word(self, wordlist):
        """
        wordlist (list): list of words (strings)
        
        Returns a word from wordlist at random
        """
        return random.choice(wordlist)

    def is_word_guessed(self, secret_word, letters_guessed):
        '''
        secret_word: string, the word the user is guessing; assumes all letters are
        lowercase
        letters_guessed: list (of letters), which letters have been guessed so far;
        assumes that all letters are lowercase
        returns: boolean, True if all the letters of secret_word are in 
        letters_guessed;
        False otherwise
        '''
        for l in secret_word:
            if l not in letters_guessed:
                return False
            else:
                continue
        return True

    def get_guessed_word(self, secret_word, letters_guessed):
        '''
        secret_word: string, the word the user is guessing
        letters_guessed: list (of letters), which letters have been guessed so far
        returns: string, comprised of letters, underscores (_), and spaces that 
        represents which letters in secret_word have been guessed so far.
        '''
        word_guessed = ''
        for l in secret_word:
            if l in letters_guessed:
                word_guessed += l + ' '
            else:
                word_guessed += '_ '
        return word_guessed

    def get_available_letters(self, letters_guessed):
        '''
        letters_guessed: list (of letters), which letters have been guessed so far
        returns: string (of letters), comprised of letters that represents which 
        letters have not yet been guessed.
        '''
        alphabet_list = list(string.ascii_lowercase)
        for l in letters_guessed:
            if l in alphabet_list:
                alphabet_list.pop(alphabet_list.index(l))
            else:
                continue
        return ', '.join(alphabet_list)

    def match_with_gaps(self, my_word, other_word, letters_guessed):
        '''
        my_word: string with _ characters, current guess of secret word
        other_word: string, regular English word
        letters_guessed: list, of letters as strings that have been guessed
        returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
        '''
        i = 0
        for char1 in my_word.replace(' ', ''):
            if char1 != other_word[i] and char1 != '_':
                return False
            elif char1 == '_' and other_word[i] in letters_guessed:
                return False
            i += 1
        return True

    def show_possible_matches(self, my_word, letters_guessed):
        '''
        my_word: string with _ characters, current guess of secret word
        letters_guessed: list, of letters as strings that have been guessed
        returns: every word in wordlist that matches 
        my_word Keep in mind that in hangman when a letter is guessed, all the
        positions at which that letter occurs in the secret word are revealed.
        Therefore, the hidden letter(_ ) cannot be one of the letters in the word
        that has already been revealed.
        '''
        wl = []
        for word in self.wordlist:
            if len(word) == len(my_word.replace(' ', '')):
                if self.match_with_gaps(my_word, word, letters_guessed) is True:
                    wl.append(word)
        return wl
