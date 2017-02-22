from tkinter import *
from glob import glob
from random import shuffle
from PIL import Image, ImageTk

class UI(Frame):
    def createWidgets(self):
        self.BATCHINPUT = Entry(self)
        self.BATCHINPUT.focus_set()
        self.BATCHINPUT.grid(row=19, column=0, columnspan=4)

        self.BATCH = Button(self)
        self.BATCH["text"] = "Generation batch"
        self.BATCH["fg"]   = "black"
        self.BATCH["command"] = self.startBatch
        self.BATCH.grid(row=18, column=0, columnspan=4)

    def startBatch(self):
        loop = 1
        if self.BATCHINPUT.get() != '':
            loop = int(self.BATCHINPUT.get())
        if (self.batchMethod):
            for x in range(loop):
                self.batchMethod()

    def setBatchMethod(self, fn):
        self.batchMethod = fn

    def preloadPieces(self, pieceslist):
        self.pImages = {}
        self.pImages['blank'] = Image.open("Eternity/blank.png")
        for x in range(256):
            self.pImages[pieceslist[x].id] = Image.open(pieceslist[x].path).resize([32, 32])
        self.createTable()

    def createTable(self):
        for i in range(256):
            self.images[i] = ImageTk.PhotoImage(self.pImages['blank'])
            self.labels[i].config(image=self.images[i])

    def drawTable(self, board):
        for i in range(256):
            piece = board[i % 16, int(i / 16)]
            if (piece is None):
                continue
            self.placePiece(piece, i % 16, int(i / 16))

    def placePiece(self, piece, x, y):
        position = 16 * y + x
        self.images[position] = ImageTk.PhotoImage(self.pImages[piece.id].rotate(-90*piece.nbofrightrotate))
        self.labels[position].config(image=self.images[position])

    def __init__(self):
        self.master = Tk()
        Frame.__init__(self, self.master)
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