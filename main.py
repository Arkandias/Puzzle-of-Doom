from patternpieces import PatternPieces
from piece import Piece
from piecesbank import PiecesBank
from ui import UI
from board import Board

def main():

    pb = PiecesBank()

    app = UI()
    app.preloadPieces(pb.pieceslist)
    pb.pieceslist[0].position['x'] = 0
    pb.pieceslist[0].position['y'] = 0
    app.placePiece(pb.pieceslist[0])
    # app.createTable(pb.pieceslist)
    app.mainloop()


if __name__ == '__main__':
    main()