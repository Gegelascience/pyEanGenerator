from enum import Enum

class EanType(Enum):
    EAN8 = 8
    EAN13 = 13

class EanCheckHelper:

    @staticmethod
    def isCorrectEan(possibleEan:str, eanTypeToCheck:EanType=None)-> bool:

        if not possibleEan:
            return False

        testLen = len(possibleEan)

        # check longueur
        try:
            testType=EanType(testLen)

            if eanTypeToCheck and not testType == eanTypeToCheck:
                return False

        except Exception:
            return False

        # check regex
        if not possibleEan.isnumeric():
            return False


        # control digit check
        eanDigitLess = possibleEan[0:testLen-1]
        possibleDigitCheck = possibleEan[testLen-1]
        if not possibleDigitCheck == EanCheckHelper.calculateDigitCheck(eanDigitLess):
            return False
            
        return True

    @staticmethod
    def calculateDigitCheck(eanDigitCheckLess:str) -> str:
        lenstrCalcul = len(eanDigitCheckLess)
        factor = 3
        somme = 0

        # check regex
        if not eanDigitCheckLess.isnumeric():
            return "KO"


        for index in range(lenstrCalcul-1,-1,-1):
            somme += int(eanDigitCheckLess[index]) * factor
            factor = 4 - factor
        
        digitCheck = str(10 - (somme % 10))

        return digitCheck

