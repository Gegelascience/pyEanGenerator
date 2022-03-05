import unittest
from EanHelper import isCorrectEan, calculateDigitCheck

class Test(unittest.TestCase):

    def test_isCorrectEan(self):
        self.assertEqual(isCorrectEan("3666154117284"),True)
        self.assertEqual(isCorrectEan("3666154117285"),False)
        self.assertEqual(isCorrectEan("36661541172n4"),False)

    def test_calculDigitCheck(self):
        self.assertEqual(calculateDigitCheck("366615411728"),"4")


    