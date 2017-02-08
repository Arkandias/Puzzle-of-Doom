import ui

class Arbiter():
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

    def isGoalAchieved(self, board):
        for y in range(16):
            for x in range(16):
                if (board[x, y] is None):
                    return False

                # Checks above cell
                if (x != 0):
                    side = board[x - 1, y].getSidePattern(2)
                    if (side or side != board[x, y].getSidePattern(0)):
                        return False
                # Checks if top side is an edge
                else:
                    if (board[x, y].getSidePattern(0) != PatternPieces.EDGE):
                        return False

                # Checks next cell
                if (y != 15):
                    side = board[x, y + 1].getSidePattern(3)
                    if (side or side != board[x, y].getSidePattern(1)):
                        return False
                # Checks if right side is an edge
                else:
                    if (board[x, y].getSidePattern(1) != PatternPieces.EDGE):
                        return False

                # Checks below cell
                if (x != 15):
                    side = board[x + 1, y].getSidePattern(0)
                    if (side or side != board[x, y].getSidePattern(2)):
                        return False
                # Checks if top side is an edge
                else:
                    if (board[x, y].getSidePattern(2) != PatternPieces.EDGE):
                        return False

                # Checks above cell
                if (x != 0):
                    side = board[x, y - 1].getSidePattern(1)
                    if (side or side != board[x, y].getSidePattern(3)):
                        return False
                # Checks if top side is an edge
                else:
                    if (board[x, y].getSidePattern(3) != PatternPieces.EDGE):
                        return False
        return True;