from Utils import setA, setC, SpecialChar
from EanCheck.EanCheckHelper import EanCheckHelper, EanType

import tkinter as tk
from tkinter import Canvas

class InvalidEan8(Exception):
    
    def __init__(self):
        self.message = "Invalid EAN8"

class Ean8Generator:

    eanValue:str = None
    barcodeValue:str = None

    def __init__(self,value:str):
        if EanCheckHelper.isCorrectEan(value, EanType.EAN8):
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
        app = tk.Tk()
        app.title(self.eanValue)
        app.geometry("700x200")
        canvas = Canvas(app)
        canvas.pack()

        width = 4
        index = 10
        for el in self.barcodeValue:
            if el == "1":
                canvas.create_line(index, 10, index, 50, width=width)
            index = index + width

        app.mainloop()


if __name__ == "__main__":
    test = Ean8Generator("36661541")
    test.showBarcode()