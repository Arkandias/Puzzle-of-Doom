import ui

class arbiter():
    def numToEdge(self, piece, i):
        if (i == 0):
            return piece.upEdge
        if (i == 1):
            return piece.rightEdge
        if (i == 2):
            return piece.downEdge
        return piece.leftEdge


    def isPlacmentValid(self, piece, board):
        nearbyPieces = []
        if (piece.position['y'] <= 0):
            nearbyPieces.append(None)
        else:
            nearbyPieces.append(board[(piece.position['x']), (piece.position['y'] - 1)])

        if (piece.position['x'] >= 15):
            nearbyPieces.append(None)
        else:
            nearbyPieces.append(board[(piece.position['x'] + 1), (piece.position['y'])])

        if (piece.position['x'] >= 15):
            nearbyPieces.append(None)
        else:
            nearbyPieces.append(board[(piece.position['x']), (piece.position['y'] + 1)])

        if (piece.position['x'] <= 0):
            nearbyPieces.append(None)
        else:
            nearbyPieces.append(board[(piece.position['x'] - 1), (piece.position['y'])])

        for i in range(0, 4):
            if (nearbyPieces[i] is not None):
               if (self.numToEdge(nearbyPieces[i], (i + 2 + nearbyPieces[i].nbofrightrotate) % 4) != self.numToEdge(piece, (
                                i + 4 - piece.nbofrightrotate) % 4)):
                    return False
        return True