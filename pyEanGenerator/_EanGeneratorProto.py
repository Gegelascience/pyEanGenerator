from _BarcodeRendering import BarcodeRendering

class EanGeneratorProto:
    '''
    abstract class for Generate EAN
    '''

    eanValue:str = None
    barcodeValue:str = None
    _renderer:BarcodeRendering = None

    def __init__(self):
        pass

    def _calculateBareCodeValue(self):
        pass

    def showBarcode(self):
        self._renderer.renderInWindow(self.eanValue, self.barcodeValue)

    def saveAsSvg(self, filePath):
        self._renderer.saveAsSvg(filePath, self.barcodeValue)

    def saveAsImg(self, filePath):
        self._renderer.saveAsImg(filePath, self.barcodeValue)