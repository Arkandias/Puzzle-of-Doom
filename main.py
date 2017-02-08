from patternpieces import PatternPieces
from piece import Piece
from piecesbank import PiecesBank
from ui import UI
from board import Board
from arbiter import Arbiter

def main():

    pb = PiecesBank()
    app = UI()
    arbiter = Arbiter()
    board = Board()

    arbiter.isGoalAchieved(board)

    ### DO NOT FUCKING REMOVE THIS. I DARE YOU. ###
    app.preloadPieces(pb.pieceslist)
    ### DO NOT FUCKING REMOVE THIS EITHER. ###
    app.mainloop()


if __name__ == '__main__':
    main()