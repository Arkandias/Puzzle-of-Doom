from tkinter import *
from glob import glob
from random import shuffle
from PIL import Image, ImageTk

class UI(Frame):
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Randomize"
        self.QUIT["fg"]   = "black"
        self.QUIT["command"] =  self.randomize

        self.QUIT.grid(row=18, column=0, columnspan=3)

        self.test = Button(self)
        self.test["text"] = "Test pieces"
        self.test["fg"]   = "red"
        self.test["command"] = self.customPiece

        self.test.grid(row=18, column=10, columnspan=3)

    def customPiece(self):
        self.pieceslist[0].position = [1, 0]
        self.pieceslist[1].position = [2, 0]
        self.createTable()


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
            if (len(self.pieceslist[i].position) != 2):
                position = i
            else:
                position = 16 * self.pieceslist[i].position[1]+self.pieceslist[i].position[0]
            self.images[position] = ImageTk.PhotoImage(self.pImages[self.pieceslist[i].id].rotate(90*self.pieceslist[i].nbofrightrotate))
            self.labels[position].config(image=self.images[position])

    def placePiece(self, piece):
        position = 16 * piece.position[1]+piece.position[0]
        self.images[position] = ImageTk.PhotoImage(self.pImages[piece.id].rotate(90*piece.nbofrightrotate))
        self.labels[position].config(image=self.images[position])

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