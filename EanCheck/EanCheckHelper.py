
class EanCheckHelper:

    @staticmethod
    def isCorrectEan(possibleEan:str)-> bool:

        testLen = len(possibleEan)

        # check longueur
        if not testLen in [8,13,14]:
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



if __name__ == "__main__":
    print(EanCheckHelper.isCorrectEan("3666154117284"))
    print(EanCheckHelper.isCorrectEan("3666154117285"))
    print(EanCheckHelper.isCorrectEan("36661541172n4"))