from tkinter import *
from glob import glob
from random import shuffle
from PIL import Image, ImageTk

class UI(Frame):
    def createWidgets(self):
        self.BATCHINPUT = Entry(self, width=7)
        self.BATCHINPUT.focus_set()
        self.BATCHINPUT.grid(row=19, column=0, columnspan=4)

        self.BATCH = Button(self)
        self.BATCH["text"] = "Generation batch"
        self.BATCH["fg"]   = "black"
        self.BATCH["command"] = self.startBatch
        self.BATCH.grid(row=18, column=0, columnspan=4)

        self.LABELFITNESS = Label(self, text="Top fitness %")
        self.LABELFITNESS.grid(row=18, column=4, columnspan=3)

        self.FITNESSINPUT = Entry(self, width=3)
        self.FITNESSINPUT.insert(0, '50')
        self.FITNESSINPUT.grid(row=19, column=4, columnspan=3)

        self.LABELMUTATION = Label(self, text="Mutation %")
        self.LABELMUTATION.grid(row=18, column=10, columnspan=3)

        self.MUTATIONINPUT = Entry(self, width=3)
        self.MUTATIONINPUT.insert(0, '5')
        self.MUTATIONINPUT.grid(row=19, column=10, columnspan=3)

    def startBatch(self):
        loop = 1
        fitness = 50
        mutation = 5
        if self.BATCHINPUT.get() != '':
            loop = int(self.BATCHINPUT.get())
        if self.FITNESSINPUT.get() != '':
            fitness = int(self.FITNESSINPUT.get())
        if self.MUTATIONINPUT.get() != '':
            mutation = int(self.MUTATIONINPUT.get())
        if (self.batchMethod):
            for x in range(loop):
                self.batchMethod(fitness, mutation)

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
            self.placePiece(piece, i % 16, int(i / 16))

    def placePiece(self, piece, x, y):
        position = 16 * y + x
        if (piece is None):
            self.images[position] = ImageTk.PhotoImage(self.pImages['blank'])
            self.labels[position].config(image=self.images[position])
        else:
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