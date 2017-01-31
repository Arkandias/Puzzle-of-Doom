from patternpieces import PatternPieces
from piece import Piece
from piecesbank import PiecesBank

def main():
    pb = PiecesBank()
    print(pb.pieceslist[200].id)

if __name__ == '__main__':
    main()