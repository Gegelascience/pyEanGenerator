from Utils import setA, setC, SpecialChar
from EanCheck import isCorrectEan, EanType
from BarcodeRendering import BarcodeRendering
from _EanGeneratorProto import EanGeneratorProto

class Ean8Generator(EanGeneratorProto):
    '''
    Generate EAN 8 barcode
    '''

    eanValue:str = None
    barcodeValue:str = None

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
    test = Ean8Generator("36661541")
    test.showBarcode()