from pyEanGenerator import isCorrectEan, EanType


from pyEanGenerator import calculateDigitCheck


from pyEanGenerator import Ean8Generator, Ean13Generator

testBareCode = Ean13Generator("3666154117284")
testBareCode.showBarcode()
testBareCode.saveAsSvg("myTest.svg")
testBareCode.saveAsImg("mytest.png")
