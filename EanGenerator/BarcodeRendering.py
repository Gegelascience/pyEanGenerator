
import tkinter as tk
from tkinter import Canvas

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