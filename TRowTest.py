import string
import re

def long_word_counter(sentence='The cow jumped over the moon.'):
    """
    This method looks for the longest word in a sentence. The return
    is a list containing the longest word and its length as an int.
    Special characters are removed from being counted.

    Example:  long_word_counter(sentence='The cow jumped over the moon.')

    """
    sentence = re.sub(r"[,.;@#?!&$]+", '', sentence).split()  #remove all punctuations from sentences
    count = 0
    lword = ''
    wordlength = 0

    for i in sentence:
        count += 1
        if len(i) > wordlength:
            lword = i
            wordlength = len(i)
    return [lword, wordlength]


def short_word_counter(sentence = 'The cow jumped over the moon.'):
    """
        This method looks for the shortest word in a sentence. The return
        is a list containing the shortest word and its length as an int.  The
        words "the" and "a" are intentionally ignored.  Special characters are
        removed from being counted.

        Example:  short_word_counter(sentence='The cow jumped over the moon.')

        """
    sentence = re.sub(r"[,.;@#?!&$]+", '', sentence).split()   #remove all punctuations from sentences
    lword = ''
    wordlength = 0

    for i in sentence:
        if (i.lower() == 'the') or (i.lower() == 'a'):   # ignore the word "the" from counting... typical use case
            continue
        elif len(i) < wordlength:
            lword = i
            wordlength = len(i)
        elif wordlength == 0:
            lword = i
            wordlength = len(i)

    return [lword, wordlength]


