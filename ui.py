from tkinter import *
from glob import glob
from random import shuffle
from PIL import Image, ImageTk

class UI(Frame):
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Randomize"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.randomize

        self.QUIT.grid(row=18, column=0, columnspan=3)

    def randomize(self):
        shuffle(self.pieceslist)
        self.createTable()

    def preloadPieces(self, pieceslist):
        self.pImages = {}
        for x in range(256):
            self.pImages[pieceslist[x].id] = Image.open(pieceslist[x].path).resize([32, 32])

    def createTable(self, pieceslist=None):
        if (pieceslist is not None):
            self.pieceslist = pieceslist
        if (self.pieceslist is None):
            return
        for i in range(len(self.pieceslist)):
            self.images[i] = ImageTk.PhotoImage(self.pImages[self.pieceslist[i].id].rotate(90*self.pieceslist[i].nbofrightrotate))
            self.labels[i].config(image=self.images[i])

    def placePiece(self, piece, x, y, orientation):
        place= x * (y % 16)

    def __init__(self):
        master = Tk()
        Frame.__init__(self, master)
        self.images = [0] * 256
        self.pImages = None
        self.labels = []
        for i in range(256):
            self.labels.append(Label(self, borderwidth=0, highlightthickness=0, width=32, height=32))
            self.labels[i].grid(row=int(i / 16), column=i % 16)
        self.scale = None
        self.pieceslist = None
        self.pack()
        self.createWidgets()