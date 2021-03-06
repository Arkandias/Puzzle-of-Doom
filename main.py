from patternpieces import PatternPieces
from piece import Piece
from piecesbank import PiecesBank
from ui import UI
from board import Board
from arbiter import Arbiter
from ai import Ai
import json
import random

def main():

    pb = PiecesBank()
    app = UI()
    ### DO NOT FUCKING REMOVE THIS. I DARE YOU. ###
    app.preloadPieces(pb.pieceslist)
    ai = Ai()
    arbiter = Arbiter()
    board = Board()

    app.setBatchMethod(lambda loop, fitness, mutation: ai.main_function(pb, app, arbiter, board, loop, fitness, mutation))
    # app.drawTable(board)
    app.drawTable(generatedSolvedPuzzle(pb))
    ### DO NOT FUCKING REMOVE THIS EITHER. ###
    app.mainloop()


def generatedSolvedPuzzle(pb):
    ret = Board()
    for y in range(16):
        for x in range(16):
            ret[x, y] = pb.pieceslist[x + y * 16]
            if (y != 0):
                if (y % 2 == 0):
                    ret[x, y].upEdge = PatternPieces.YELLOWFLOWERINBLUE
                else:
                    ret[x, y].upEdge = PatternPieces.BLUESTARINYELLOW
            else:
                ret[x, y].upEdge = PatternPieces.EDGE

            if (x != 15):
                if (x % 2 == 0):
                    ret[x, y].rightEdge = PatternPieces.BLUEGEARINPINK
                else:
                    ret[x, y].rightEdge = PatternPieces.YELLOWSTARINPURPLE
            else:
                ret[x, y].rightEdge = PatternPieces.EDGE

            if (y != 15):
                if (y % 2 == 1):
                    ret[x, y].downEdge = PatternPieces.YELLOWFLOWERINBLUE
                else:
                    ret[x, y].downEdge = PatternPieces.BLUESTARINYELLOW
            else:
                ret[x, y].downEdge = PatternPieces.EDGE

            if (x != 0):
                if (x % 2 == 1):
                    ret[x, y].leftEdge = PatternPieces.BLUEGEARINPINK
                else:
                    ret[x, y].leftEdge = PatternPieces.YELLOWSTARINPURPLE
            else:
                ret[x, y].leftEdge = PatternPieces.EDGE
    return ret

if __name__ == '__main__':
    main()