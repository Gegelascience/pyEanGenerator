import unittest
from EanCheckHelper import EanCheckHelper, EanType

class TestEanCheckHelper(unittest.TestCase):

    def test_isCorrectEan_noerror(self):
        self.assertEqual(EanCheckHelper.isCorrectEan("3666154117284"),True)
        self.assertEqual(EanCheckHelper.isCorrectEan("3666154117284", EanType.EAN13),True)
        

    def test_isCorrectEan_error(self):
        self.assertEqual(EanCheckHelper.isCorrectEan("3666154117284", EanType.EAN8),False)
        self.assertEqual(EanCheckHelper.isCorrectEan("3666154117285"),False)
        self.assertEqual(EanCheckHelper.isCorrectEan("36661541172n4"),False)
        self.assertEqual(EanCheckHelper.isCorrectEan(None),False)

    def test_calculDigitCheck_noerror(self):
        self.assertEqual(EanCheckHelper.calculateDigitCheck("366615411728"),"4")

    def test_calculDigitCheck_error(self):
        self.assertRaises(TypeError,EanCheckHelper.calculateDigitCheck, None)



if __name__ == "__main__":
    unittest.main()


    