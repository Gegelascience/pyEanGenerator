import unittest
from EanCheckHelper import EanCheckHelper

class Test(unittest.TestCase):

    def test_isCorrectEan(self):
        self.assertEqual(EanCheckHelper.isCorrectEan("3666154117284"),True)
        self.assertEqual(EanCheckHelper.isCorrectEan("3666154117285"),False)
        self.assertEqual(EanCheckHelper.isCorrectEan("36661541172n4"),False)

    def test_calculDigitCheck(self):
        self.assertEqual(EanCheckHelper.calculateDigitCheck("366615411728"),"4")




if __name__ == "__main__":
    unittest.main()


    