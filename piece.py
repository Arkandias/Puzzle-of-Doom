from patternpieces import PatternPieces


class Piece:
    def __init__(self, idpiece, left=PatternPieces.EDGE, up=PatternPieces.EDGE,
                 right=PatternPieces.EDGE, down=PatternPieces.EDGE):
        self.id = idpiece
        self.leftEdge = left
        self.upEdge = up
        self.rightEdge = right
        self.downEdge = down
        self.position = list()
        self.nbofrightrotate = 0
        self.imgpath = None