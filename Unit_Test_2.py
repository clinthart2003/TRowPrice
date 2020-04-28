from TRowTest import *

test_sentances_long = [['The cow jumped over the moon.', 'jumped', 6],
                       ['The cow jumped over the moon?', 'jumped', 6]
                       ]


test_sentances_short = [['Add a method that returns the shortest word and length with unit tests!', 'Sentance', 8],
                        ['Add a method that returns the shortest word and length with unit tests!', 'Add', 3]
                        ]

def unittest():
    """
    This is a condensed version of a set of tests that uses 1 method for execution.  the
    list "test_sentances" contains a sentance, the expected word and its length.

    Example results:
    test Passed: jumped, 6
    test Passed: cow, 3
    Test Failed: Add, 3   Intentionally FAILED test
    test Passed: shortest, 8
    """
    for test in test_sentances_long:
        try:
            results = (long_word_counter(test[0]))
            if (results[0] == test[1]) and (results[1]==test[2]):
                print ("test Passed: " + results[0] + ", " + str(results[1]))
            else:
                print ("test Failed: " + results[0] + ", " + str(results[1]) + " expected: " + test[1] +", " + str(test[2]))
        except Exception as e:
            print (e)

    for test in test_sentances_short:
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
