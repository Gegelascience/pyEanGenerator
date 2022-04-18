
import os
import tkinter as tk
from tkinter import Canvas
from xml.etree import ElementTree as ET

class BarcodeRendering:
    barcodeValue:str = None
    eanValue:str = None
    width:str = 4
    color:str = "black"

    def __init__(self, barcodeValue:str, eanValue:str, width:int=4, color:str="black"):
        self.barcodeValue = barcodeValue
        self.eanValue = eanValue
        self.width = width
        self.color = color

    
    def renderInWindow(self):
        app = tk.Tk()
        app.title(self.eanValue)
        app.geometry("700x200")
        canvas = Canvas(app)
        canvas.pack()

        index = 10
        for el in self.barcodeValue:
            if el == "1":
                canvas.create_line(index, 10, index, 50, width=self.width, fill=self.color)
            index = index + self.width

        app.mainloop()


    def saveAsSvg(self,filePath):
        initialStr = '''
        <svg version='1.1' baseProfile='full' width='700' height='200' xmlns='http://www.w3.org/2000/svg'>
        </svg>'''
        root = ET.XML(initialStr)
        barcodeZone = ET.SubElement(root,"g")
        barcodeZone.set("stroke", self.color)
        index = 10
        for el in self.barcodeValue:
            if el == "1":
                line = ET.SubElement(barcodeZone,"line")
                line.set("stroke-width",str(self.width))
                line.set("y1",str(10))
                line.set("x1",str(index))
                line.set("y2",str(50))
                line.set("x2",str(index))
            index = index + self.width

        tree = ET.ElementTree(root)
        ET.register_namespace("","http://www.w3.org/2000/svg")

        tree.write(filePath, encoding="utf-8",xml_declaration=True)
