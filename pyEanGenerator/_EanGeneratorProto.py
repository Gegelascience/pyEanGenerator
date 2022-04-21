from _BarcodeRendering import BarcodeRendering

class EanGeneratorProto:
    '''
    abstract class for Generate EAN
    '''

    _renderer:BarcodeRendering = None

    def __init__(self):
        pass

    def _calculateBareCodeValue(self):
        pass

    def showBarcode(self):
        self._renderer.renderInWindow()

    def saveAsSvg(self, filePath):
        self._renderer.saveAsSvg(filePath)