from TRowTest import *

test_sentences_long = [['The cow jumped over the moon.', 'jumped', 6],
                       ["Clinton's sister just had from COVAD-19!!!", 'Clinton\'s', 9]
                       ]


test_sentences_short = [['Add a method that returns the shortest word and length with unit tests!', 'Add', 3],
                        ["Clinton's sister just had from COVAD-19!!!", 'had', 3]
                        ]

def unittest():
    """
    This is a condensed version of a set of tests that uses 1 method for execution.  the
    list "test_sentences" contains a sentence, the expected word and its length.

    Example results:
    test Passed: jumped, 6
    test Passed: cow, 3
    Test Failed: Add, 3   Intentionally FAILED test
    test Passed: shortest, 8
    """
    for test in test_sentences_long:
        try:
            results = (long_word_counter(test[0]))
            if (results[0] == test[1]) and (results[1]==test[2]):
                print ("test Passed: " + results[0] + ", " + str(results[1]))
            else:
                print ("test Failed: " + results[0] + ", " + str(results[1]) + " expected: " + test[1] +", " + str(test[2]))
        except Exception as e:
            print (e)

    for test in test_sentences_short:
        try:
            results = (short_word_counter(test[0]))
            if (results[0] == test[1]) and (results[1]==test[2]):
                print ("test Passed: " + results[0] + ", " + str(results[1]))
            else:
                print("test Failed: " + results[0] + ", " + str(results[1]) + " expected: " + test[1] + ", " + str(test[2]))
        except Exception as e:
            print (e)

if __name__ == '__main__':
    unittest()
