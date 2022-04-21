from Utils import setA, setB, setC, SpecialChar
from EanCheck import isCorrectEan, EanType
from _BarcodeRendering import BarcodeRendering
from _EanGeneratorProto import EanGeneratorProto

class Ean13Generator(EanGeneratorProto):
    '''
    Generate EAN 13 barcode
    '''

    def __init__(self,value:str):
        if isCorrectEan(value, EanType.EAN13):
            self.eanValue = value
            self._calculateBareCodeValue()
            self._renderer = BarcodeRendering(self.barcodeValue,self.eanValue)

        else:
            raise Exception("Invalid EAN13")


    def _calculateBareCodeValue(self):
        '''
        Calculate bits encoding barcode from ean value
        '''
        self.barcodeValue = SpecialChar.START.value

        firstPartRaw = self.eanValue[1:7]
        secondPartRaw = self.eanValue[7:]

        prefix = self.eanValue[0]

        for index, element in enumerate(firstPartRaw):
            setToApply = self.__calculateSetFromPrefix(prefix,index)
            if setToApply == "A":
                self.barcodeValue = self.barcodeValue + setA[element]
            else:
                self.barcodeValue = self.barcodeValue + setB[element]

        self.barcodeValue = self.barcodeValue + SpecialChar.CENTER.value

        for element in secondPartRaw:
            self.barcodeValue = self.barcodeValue + setC[element]

        self.barcodeValue = self.barcodeValue + SpecialChar.END.value

    def __calculateSetFromPrefix(self, prefix:str, index:int) -> str:
        '''
        Found odd set (set A) or even set (set B) by prefix value
        '''
        if index == 0:
            return "A"

        if prefix == 0:
            return "A"

        elif prefix == "1":
            return "A" if index in [1,3] else "B"

        elif prefix == "2":
            return "A" if index in [1,4] else "B"

        elif prefix == "3":
            return "A" if index in [1,5] else "B"

        elif prefix == "4":
            return "A" if index in [2,3] else "B"

        elif prefix == "5":
            return "A" if index in [3,4] else "B"

        elif prefix == "6":
            return "A" if index in [4,5] else "B"

        elif prefix == "7":
            return "A" if index in [2,4] else "B"

        elif prefix == "8":
            return "A" if index in [2,5] else "B"

        elif prefix == "9":
            return "A" if index in [3,5] else "B"

class Ean8Generator(EanGeneratorProto):
    '''
    Generate EAN 8 barcode
    '''

    def __init__(self,value:str):
        if isCorrectEan(value, EanType.EAN8):
            self.eanValue = value
            self._calculateBareCodeValue()
            self._renderer = BarcodeRendering(self.barcodeValue,self.eanValue)

        else:
            raise Exception("Invalid EAN8")

    def _calculateBareCodeValue(self):
        self.barcodeValue = SpecialChar.START.value

        firstPartRaw = self.eanValue[:4]
        secondPartRaw = self.eanValue[4:]

        for element in firstPartRaw:
            self.barcodeValue = self.barcodeValue + setA[element]

        self.barcodeValue = self.barcodeValue + SpecialChar.CENTER.value

        for element in secondPartRaw:
            self.barcodeValue = self.barcodeValue + setC[element]

        self.barcodeValue = self.barcodeValue + SpecialChar.END.value

if __name__ == "__main__":
    test = Ean13Generator("3666154117284")
    test.showBarcode()
    test.saveAsSvg("myTest.svg")

    test.saveAsImg("mytest.png")

    test2 = Ean8Generator("36661541")
    test2.showBarcode()
    test2.saveAsSvg("myTest2.svg")