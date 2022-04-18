from Utils import setA, setC, SpecialChar

from EanCheck.EanCheckHelper import EanCheckHelper, EanType


class InvalidEan8(Exception):

    pass

class Ean13Generator:

    eanValue:str = None

    def __init__(self,value:str):
        if EanCheckHelper.isCorrectEan(value, EanType.EAN8):
            self.eanValue = value

        else:
            raise InvalidEan8()