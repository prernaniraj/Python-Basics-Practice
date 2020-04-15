import unittest
import guessNum

class GuessNumTest(unittest.TestCase):
    def guessNum_Test(self):
        '''String input test '''
        num = "asdf"
        result = guessNum.guessNumber(num)
        self.assertEqual(result,'please enter a number')

    def guessNum_Test1(self):
        ''' None Input test '''
        num = None
        result = guessNum.guessNumber(num)
        self.assertEqual(result,'please enter a number')


if __name__ == "__main__":
    unittest.main()