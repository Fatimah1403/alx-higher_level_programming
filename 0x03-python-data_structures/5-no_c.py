#!/usr/bin/python3

def no_c(my_string):
    new_words = my_string.translate({ord('c'): None})
    new_words = new_words.translate({ord('C'): None})
    return new_words
