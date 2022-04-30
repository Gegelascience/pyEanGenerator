from src.pyEanGenerator import isCorrectEan, EanType


from src.pyEanGenerator import calculateDigitCheck


from src.pyEanGenerator import Ean8Generator, Ean13Generator

testBareCode = Ean13Generator("3666154117284")
testBareCode.showBarcode()
testBareCode.saveAsSvg("myTest.svg")
testBareCode.saveAsImg("mytest.png")
