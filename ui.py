from tkinter import *
from glob import glob

class UI(Frame):
    # def createWidgets(self):
    #     self.QUIT = Button(self)
    #     self.QUIT["text"] = "X"
    #     self.QUIT["fg"]   = "red"
    #     self.QUIT["command"] =  self.quit

    #     self.QUIT.grid(row=17, column=1)

    def createTable(self, bank):
        self.zoom = None
        self.images = [PhotoImage()] * 256
        for i in range(len(bank.pieceslist)):
            self.images[i].configure(file=bank.pieceslist[i].path)
            if (self.zoom is None):
                self.zoom = 32 / self.images[i].width()
            self.images[i] = self.images[i].subsample(9, 9)
            imageLabel = Label(self, image=self.images[i], borderwidth=0, highlightthickness=0)
            imageLabel.grid(row=int(i / 16) + 1, column=i % 16)

    def __init__(self):
        master = Tk()
        Frame.__init__(self, master)
        self.pack()

        # self.createWidgets()
