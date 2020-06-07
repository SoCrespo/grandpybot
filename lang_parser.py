# coding: utf-8

from string import punctuation
import stop_words as sw

signs = punctuation.replace('-', '')
separators = str.maketrans(signs, " " * len(signs))
stop_words = sw.base + sw.salutations


class LangParser:

    def __init__(self):
        pass

    def find_the_word(self, text):
        '''
        Take a sentence (string, can be a single word) as argument.
        Return the most relevant word (string) as a location name.
        '''
        list_of_words = self._splitter(text)
        list_of_relevant_words = self._remove_stop_words(list_of_words)
        best_word = self._word_after_adress(list_of_relevant_words)
        if best_word is None:
            best_word = self._choose_upper_or_last(list_of_relevant_words)
        return best_word

    def _splitter(self, text):
        '''
        Take a string as argument.
        Return the list splitted with all punctuation signs (except "-")
        as separators.
        '''
        return text.translate(separators).split()

    def _remove_stop_words(self, list_of_words):
        '''
        Take a list of words (strings) as argument.
        Return a list of this list's items that are not in stop_word lists
        (case insensive comparison).
        '''
        return [word for word in list_of_words
                if word.lower() not in stop_words]

    def _word_after_adress(self, list_of_words):
        """
        Take a list of words as argument.
        If the word "adresse" is in the list, return the next word.
        """
        for word in list_of_words:
            if word.lower() == "adresse":
                return list_of_words[list_of_words.index(word) + 1]

    def _choose_upper_or_last(self, list_of_words):
        '''
        Take a list of words as argument.
        Return the upper-case word if there's only one,
        or the last upper-case if there are several,
        or the last word if none is upper-case.
        '''
        rev_list = list(reversed(list_of_words))
        word = rev_list[0]
        for item in rev_list[1:]:
            if item[0].isupper():
                word = item
                break
        return word


if __name__ == "__main__":
    pass
