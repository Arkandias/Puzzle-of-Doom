from tkinter import *
from glob import glob
from random import shuffle
from PIL import Image, ImageTk

class UI(Frame):
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Button"
        self.QUIT["fg"]   = "black"
        # self.QUIT["command"] = self.randomize

        self.QUIT.grid(row=18, column=0, columnspan=3)

    def setButtonBehaviour(self, name, fn):
        self.QUIT["text"] = name
        self.QUIT["command"] = fn

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