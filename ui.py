from tkinter import *
from glob import glob
from random import shuffle

class UI(Frame):
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Randomize"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.randomize

        self.QUIT.grid(row=17, column=0, columnspan=3)

    def randomize(self):
        shuffle(self.bank.pieceslist)
        self.createTable(self.bank)
        pass

    def createTable(self, bank):
        self.bank = bank
        self.images = [PhotoImage()] * 256
        for i in range(len(bank.pieceslist)):
            self.images[i].configure(file=bank.pieceslist[i].path)
            if (self.scale is None):
                self.scale = int(self.images[i].width() / 32)
            self.images[i] = self.images[i].subsample(self.scale, self.scale)
            imageLabel = Label(self, image=self.images[i], borderwidth=0, highlightthickness=0)
            imageLabel.grid(row=int(i / 16) + 1, column=i % 16)

    def __init__(self):
        master = Tk()
        Frame.__init__(self, master)
        self.scale = None
        self.pack()
        self.createWidgets()