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
        if (i.lower() == 'the') or (i.lower() == 'a'):   # ignore the words "the" and "a" from counting... typical usecase
            continue
        elif count == 0:
            lword = i
            wordlength = len(i)
        if len(i) < wordlength:
            lword = i
            wordlength = len(i)
        count += 1
    return [lword, wordlength]


#unittests
results = (long_word_counter(sentance='The cow jumped over the moon.'))
if results[0] != 'jumped' and results[1]!='6':
    print ("test Failed")
    print(results)
else:
    print ("test PASSED")
    print(results)

results = (short_word_counter(sentance='The cow jumped over the moon?'))
if results[0] != 'cow' and results[1]!='3':
    print ("test Failed")
    print (results)
else:
    print ("Test PASSED")
    print(results)

results = (short_word_counter(sentance='Add a method that returns the shortest word and length with unit tests!'))
if results[0] != 'Add' and results[1]!='3':
    print ("test Failed")
    print (results)
else:
    print ("Test PASSED")
    print(results)

results = (long_word_counter(sentance='Add a method that returns the shortest word and length with unit tests!'))
if results[0] != 'shortest' and results[1]!='8':
    print ("test Failed")
    print (results)
else:
    print ("Test PASSED")
    print(results)
