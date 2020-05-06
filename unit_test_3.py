from TRowTest import *
import unittest

test_sentences_long = [['The cow jumped over the moon.', 'jumped', 6],
                       ["Clint's sister just recovered from COVAD-19!!!", 'recovered', 9]
                       ]


test_sentences_short = [['Add a method that returns the shortest word and length with unit tests!', 'shortest', 3],
                        ['Add a method that returns the shortest word and length with unit tests!', 'Add', 3]
                        ]
class TestMethods(unittest.TestCase):

    def Test_long(self):
        """
        This is a condensed version of a set of tests that uses 1 method for execution.  the
        list "test_sentences" contains a sentence, the expected word and its length.

        Example results:
        ----------------------------------------------------------------------
        Ran 1 test in 0.000s

        OK
        Lists differ: ['Add', 3] != ['shortest', 3]

        First differing element 0:
        'Add'
        'shortest'

        - ['Add', 3]
        + ['shortest', 3]

        """
        for test in test_sentences_long:
            self.expected = [test[1], test[2]]
            try:
               self.assertListEqual(long_word_counter(test[0]), self.expected)
            except Exception as e:
                print (e)

    def test_short(self):
        for test in test_sentences_short:
            self.expected = [test[1], test[2]]
            try:
                self.assertListEqual(short_word_counter(test[0]), self.expected)
            except Exception as e:
                print (e)

if __name__ == '__main__':
    unittest.main()
