# coding: utf-8

from string import punctuation
from backend import stop_words as sw

signs = punctuation.replace('-', '')
separators = str.maketrans(signs, " " * len(signs))
stop_words = sw.general



def find_relevant_expression(text):
    '''
    Take a sentence (string, can be a single word) as argument.
    Return the most relevant string as a location name.
    '''
    list_of_words = _splitter(text)
    list_of_relevant_words = _remove_stop_words(list_of_words)
    if len(list_of_relevant_words) < 4:
        expression = " ".join(list_of_relevant_words)
    else:
        expression = " ".join(list_of_relevant_words[-4:])
    return expression


def _splitter(text):
    '''
    Take a string as argument.
    Return the list splitted with all punctuation signs (except "-")
    as separators.
    '''
    return text.translate(separators).split()


def _remove_stop_words(list_of_words):
    '''
    Take a list of words (strings) as argument.
    Return a list of this list's items that are not stop words
    (case insensive comparison).
    '''
    return [word for word in list_of_words
            if word.lower() not in stop_words]
