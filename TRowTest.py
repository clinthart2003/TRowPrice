import string
import re

def long_word_counter(sentance='The cow jumped over the moon.'):
    """
    This method looks for the longest word in a sentance. The return
    is a list containing the longest word and its length as an int.
    Special characters are removed from being counted.

    Example:  long_word_counter(sentance='The cow jumped over the moon.')

    """
    sentance = re.sub(r"[,.;@#?!&$]+", '', sentance).split()  #remove all punctuations from sentances
    count = 0
    lword = ''
    wordlength = 0

    for i in sentance:
        count += 1
        if len(i) > wordlength:
            lword = i
            wordlength = len(i)
    return [lword, wordlength]


def short_word_counter(sentance = 'The cow jumped over the moon.'):
    """
        This method looks for the shortest word in a sentance. The return
        is a list containing the shortest word and its length as an int.  The
        words "the" and "a" are intentionally ignored.  Special characters are
        removed from being counted.

        Example:  short_word_counter(sentance='The cow jumped over the moon.')

        """
    sentance = re.sub(r"[,.;@#?!&$]+", '', sentance).split()   #remove all punctuations from sentances
    count = 0
    lword = ''
    wordlength = 0

    for i in sentance:
        if (i.lower() == 'the') or (i.lower() == 'a'):   # ignore the word "the" from counting... typical usecase
            continue
        elif count == 0:
            lword = i
            wordlength = len(i)
        if len(i) < wordlength:
            lword = i
            wordlength = len(i)
        count += 1
    return [lword, wordlength]


