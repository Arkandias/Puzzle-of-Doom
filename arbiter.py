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
        nearbyPieces[0] = board[(piece.position.x), (piece.position.y <= 0 if NULL else piece.position.y - 1)]
        nearbyPieces[1] = board[(piece.position.x >= 15 if NULL else piece.position.x + 1), (piece.position.y)]
        nearbyPieces[2] = board[(piece.position.x), (piece.position.y >= 15 if NULL else piece.position.y + 1)]
        nearbyPieces[3] = board[(piece.position.x <= 0 if NULL else piece.position.x - 1), (piece.position.y)]

        for i in range(0, 4):
            if (nearbyPieces[i] is not None):
                if (numToEdge(nearbyPieces[i], (i + 2 + nearbyPieces.nbofrightrotate) % 4 != numToEdge(piece, (
                                i + 4 - piece.nbofrightrotate) % 4))):
                    return false
        return true