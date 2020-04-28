from TRowTest import *

def unittest():

    try:
        results = (long_word_counter(sentance = 'The cow jumped over the moon.'))
        if (results[0] == 'jumped') and (results[1]==6):
            print ("test Passed: " + results[0] + ", " + str(results[1]))
        else:
            print ("test Failed: " + results[0] + ", " + str(results[1]))
    except Exception as e:
        print (e)

    try:
        results = (short_word_counter(sentance='The cow jumped over the moon?'))
        if results[0] == 'cow' and results[1]==3:
            print ("test Passed: " + results[0] + ", " + str(results[1]))
        else:
            print ("Test Failed: " + results[0] + ", " + str(results[1]))
    except Exception as e:
        print (e)

    results = (short_word_counter(sentance='Add a method that returns the shortest word and length with unit tests!'))
    if (results[0] == 'Add') and (results[1]==9):
        print ("test Passed: " + results[0] + ", " + str(results[1]))
    else:
        print ("Test Failed: " + results[0] + ", " + str(results[1]) + "   Intentionally FAILED test")

    try:
        results = (long_word_counter(sentance='Add a method that returns the shortest word and length with unit tests!'))
        if results[0] == 'shortest' and results[1]==8:
            print ("test Passed: " + results[0] + ", " + str(results[1]))
        else:
            print ("Test Failed: " + results[0] + ", " + str(results[1]))
    except Exception as e:
        print (e)

if __name__ == '__main__':
    unittest()
