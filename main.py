from patternpieces import PatternPieces
from piece import Piece
from piecesbank import PiecesBank
from ui import UI
from board import Board

def main():

    pb = PiecesBank()
    app = UI()
    board = Board()

    app.preloadPieces(pb.pieceslist)
    app.mainloop()


if __name__ == '__main__':
    main()