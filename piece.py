from patternpieces import PatternPieces


class Piece:
    def __init__(self, idpiece, left=PatternPieces.EDGE, up=PatternPieces.EDGE,
                 right=PatternPieces.EDGE, down=PatternPieces.EDGE):
        self.id = idpiece
        self.leftEdge = left
        self.upEdge = up
        self.rightEdge = right
        self.downEdge = down
        self.position = {"x":None, "y":None}
        self.nbofrightrotate = 0
        self.imgpath = None

    def switch(self, x):
        return {
            0: self.upEdge,
            1: self.rightEdge,
            2: self.downEdge,
            3: self.leftEdge
        }.get(x, False)

    def getSidePattern(self, rotation):
        rotation = rotation - self.nbofrightrotate if rotation - self.nbofrightrotate >= 0 else rotation - self.nbofrightrotate + 4
        return self.switch(rotation)
