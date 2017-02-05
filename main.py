from patternpieces import PatternPieces
from piece import Piece
from piecesbank import PiecesBank
from ui import UI
from board import Board

def main():

    pb = PiecesBank()
    app = UI()
    ### DO NOT FUCKING REMOVE THIS. I DARE YOU. ###
    app.preloadPieces(pb.pieceslist)
    board = Board()

    ### DO NOT FUCKING REMOVE THIS EITHER. ###
    app.mainloop()


if __name__ == '__main__':
    main()