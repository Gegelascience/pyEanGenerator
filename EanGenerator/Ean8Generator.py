from Utils import setA, setC, SpecialChar
from EanCheck.EanCheckHelper import isCorrectEan, EanType
from BarcodeRendering import BarcodeRendering

class InvalidEan8(Exception):
    
    def __init__(self):
        self.message = "Invalid EAN8"

class Ean8Generator:

    eanValue:str = None
    barcodeValue:str = None

    def __init__(self,value:str):
        if isCorrectEan(value, EanType.EAN8):
            self.eanValue = value
            self.__calculateBareCodeValue()

        else:
            raise InvalidEan8

    def __calculateBareCodeValue(self):
        self.barcodeValue = SpecialChar.START.value

        firstPartRaw = self.eanValue[:4]
        secondPartRaw = self.eanValue[4:]

        for element in firstPartRaw:
            self.barcodeValue = self.barcodeValue + setA[element]

        self.barcodeValue = self.barcodeValue + SpecialChar.CENTER.value

        for element in secondPartRaw:
            self.barcodeValue = self.barcodeValue + setC[element]

        self.barcodeValue = self.barcodeValue + SpecialChar.END.value

    def showBarcode(self):
        renderer = BarcodeRendering(self.barcodeValue,self.eanValue,4,"black")
        renderer.renderInWindow()


if __name__ == "__main__":
    test = Ean8Generator("36661541")
    test.showBarcode()