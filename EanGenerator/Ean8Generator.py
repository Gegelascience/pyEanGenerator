from Utils import setA, setC, SpecialChar
from EanCheck.EanCheckHelper import isCorrectEan, EanType
from BarcodeRendering import BarcodeRendering

class Ean8Generator:

    eanValue:str = None
    barcodeValue:str = None
    __renderer:BarcodeRendering = None

    def __init__(self,value:str):
        if isCorrectEan(value, EanType.EAN8):
            self.eanValue = value
            self.__calculateBareCodeValue()
            self.__renderer = BarcodeRendering(self.barcodeValue,self.eanValue)

        else:
            raise Exception("Invalid EAN8")

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
        self.__renderer.renderInWindow()

    def saveAsSvg(self, filePath):
        self.__renderer.saveAsSvg(filePath)


if __name__ == "__main__":
    test = Ean8Generator("36661541")
    test.showBarcode()