# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 00:13:09 2019
@author: Metin Mert Akçay
"""

from collections import OrderedDict  # ordered dictionary


TURKS_CHARS = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z", "<", ">", ""]
VOWELS = ["a", "e", "ı", "i", "o", "ö", "u", "ü", ""]
CORPUS = "corpus.txt"
INITIAL_STATE = 1       # The initial state value is set to 1 since '<' will be in the first place.


"""
    This function allows words to be read from the prepared corpus and seperate by space.
    @return: all words
"""
def read_words():
    with open(CORPUS, 'r', encoding = "iso-8859-9") as file:
        return file.read().rsplit()


"""
    This function allows us to convert the words in the word list to a specific format.
    @param words: list of words read from corpus
    
    Format = <word>
"""
def transform_words(words):
    for i, word in enumerate(words):
        words[i] = '<' + word + '>'


"""
    This function is used to initialize the dictionary.
    @return bigram_dict: dictionary to hold the number of passes of character bigram.
"""
def initialize_dict():
    bigram_dict = OrderedDict()
    for i in TURKS_CHARS:
        for j in TURKS_CHARS:
            bigram_dict[i, j] = 0
    return bigram_dict


"""
    This function is used to divide the word into bigrams. (if two character is consonant it divide two part (char1, char2) ---> (char1, ""), ("", char2))
    @param word: word
    @return bigram: word bigrams
"""
def find_bigrams(word):
    i = 1
    bigram = []
    while i < len(word):
        # two consonant character check
        if (word[i] in VOWELS) or (word[i - 1] in VOWELS):
            bigram.append((word[i - 1], word[i]))
        else:
            bigram.append((word[i - 1], ""))
            bigram.append(("", word[i]))
        i += 1
    return bigram
    

"""
    This function is used to count character bigram.
    @param words: list of words read from corpus
    @param bigram_dict: dictionary of character bigram and passing numbers in corpus.
"""
def count_character_bigram(words, bigram_dict):
    for i, word in enumerate(words):
        bigrams = find_bigrams(word)
        for bigram in bigrams:
            if bigram in bigram_dict:
                bigram_dict[bigram] += 1


"""
    This function is used to calculate the probability of finding bigram.
    @param bigram_dict: dictionary of character bigram and passing probability in corpus.
"""
def find_probability_character_bigram(bigram_dict):
    for i, char in enumerate(TURKS_CHARS):
        total = 0
        for j in range(0, len(TURKS_CHARS)): 
            total += list(bigram_dict.values())[i * len(TURKS_CHARS) + j]
        for j in range(0, len(TURKS_CHARS)):
            try:
                bigram_dict[list(bigram_dict.keys())[i * len(TURKS_CHARS) + j]] = round(list(bigram_dict.values())[i * len(TURKS_CHARS) + j] / total, 3)
            except ZeroDivisionError:
                bigram_dict[list(bigram_dict.keys())[i * len(TURKS_CHARS) + j]] = 0


"""
    This function is used to generate word.
    @param consonants: consonant characters
    @param vowels: vowel characters
    @return: generated word
"""
def generate_result_word(consonants, vowels):
   res = ''
   
   # start and end character is excluded during word creation.
   i = 1
   while i < len(consonants) - 1:
       if vowels[i - 1] != 'w':
           res += vowels[i - 1]
       res += consonants[i]
       i = i + 1
   
   if vowels[i - 1] != 'w':
       res += vowels[i - 1]
   
   return res
  

"""
    This function is used to check input characters
    @param consonants: It is the parameter which is entered by user
    @return True: if parameter has problem, False everything is OK.
"""
def check_input_has_vowel_or_digit(consonants):
    # empty charcter check
    if(len(consonants) == 2):
        return True
    
    for char in consonants:
        # vowel character check
        if char in VOWELS:
            return True
        # digit number check
        if char.isdigit():
            return True
    return False


"""
    This function is used to complete vowel characters.
    @param bigram_dict: this parameter is holding the probability of character bigrams.
"""
def vowel_completion(bigram_dict):
    consonants = '<' + input("Enter consonant letter..>") + '>'
    while check_input_has_vowel_or_digit(consonants):
        consonants = '<' + input("Enter consonant letter..>") + '>'
    
    # initial state is set to 1 because all words will start with the '<' character.
    # left side shows us vowel character sequence and right side shows us probability
    sequence_probability_list = [[[] , INITIAL_STATE]]
    
    i = 0
    # last character is a stop character '>', there is no need to process it.
    while i < len(consonants) - 1:
        result_list = []
        # all vowels are iterated and find possibility.
        for j in range(len(VOWELS)):
            sequence = sequence_probability_list[0][0].copy()
            # empty character is represented by the w.
            if(VOWELS[j] == ""):
                sequence.append("w")
            else:
                sequence.append(VOWELS[j])
            
            # assumption
            if len(sequence) >= 2 and (sequence[-1] == "w" and sequence[-2] == "w"):
                probability = sequence_probability_list[0][1] * bigram_dict[consonants[i], VOWELS[j]] / 100
            else:
                probability = sequence_probability_list[0][1] * bigram_dict[consonants[i], VOWELS[j]]
            result_list.append([sequence, probability])
        
        # check first letter is ğ
        if i == 0 and consonants[i + 1] == 'ğ':
            del result_list[-1]
        
        # assign the one with the highest probability.
        result_list.sort(key = lambda result_list: result_list[1], reverse=True)   
        sequence_probability_list = [result_list[0].copy()]
        i = i + 1
    
    # the most recent word is printed.
    word = generate_result_word(consonants, sequence_probability_list[0][0])
    print("Generated word is --> " + word)
    

"""
    This is where the code starts.
"""
if __name__ == '__main__':
    print("Please waiting. Corpus is loading...")
    words = read_words()
    transform_words(words)
    bigram_dict = initialize_dict()
    count_character_bigram(words, bigram_dict)
    find_probability_character_bigram(bigram_dict)
    
    cont = 'c'
    while cont == 'c' or cont == 'C':
        vowel_completion(bigram_dict)
        cont = input("If you want to continue, please enter 'c' or 'C' character..>")
    