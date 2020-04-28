import string
import re

def long_word_counter(sentance='The cow jumped over the moon.'):
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


