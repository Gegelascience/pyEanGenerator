from Utils import setA, setC, SpecialChar

from EanCheck.EanCheckHelper import EanCheckHelper, EanType


class InvalidEan8(Exception):
    
    def __init__(self):
        self.message = "Invalid EAN 8"

class Ean8Generator:

    eanValue:str = None

    def __init__(self,value:str):
        if EanCheckHelper.isCorrectEan(value, EanType.EAN8):
            self.eanValue = value

        else:
            raise InvalidEan8


Ean8Generator(None)