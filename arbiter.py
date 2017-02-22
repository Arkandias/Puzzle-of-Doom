from patternpieces import PatternPieces


class Arbiter:
    #adding x, y because for checking the piece must not be set
    #Adding True instead of None for walls and keeping none for no piece
    #TODO Factorize this fonction
    def is_placement_valid(self, piece, board, x, y):
        nearbyPieces = []
        mismatch = False
        if y <= 0:
            nearbyPieces.append(True)
        else:
            nearbyPieces.append(board[x, y - 1])

        if x >= 15:
            nearbyPieces.append(True)
        else:
            nearbyPieces.append(board[x + 1, y])

        if y >= 15:
            nearbyPieces.append(True)
        else:
            nearbyPieces.append(board[x, y + 1])

        if x <= 0:
            nearbyPieces.append(True)
        else:
            nearbyPieces.append(board[x - 1, y])
        for rotatetry in range(0, 4):
            piece.nbofrightrotate = rotatetry
            for i in range(0, 4):
                if nearbyPieces[i] is True:
                    if piece.getSidePattern(i) != PatternPieces.EDGE:
                        mismatch = True
                        break
                elif nearbyPieces[i] is not None:
                    if nearbyPieces[i].getSidePattern(i - 2) != piece.getSidePattern(i):
                        mismatch = True
                        break
                else:
                    if piece.getSidePattern(i) == PatternPieces.EDGE:
                        mismatch = True
                        break
            if mismatch is False:
                return True
            else:
                mismatch = False
        return False

    def check_and_place(self, piece, board, x, y):
        if self.is_placement_valid(piece, board, x, y):
            board[x, y] = piece
            piece.placed = True
            return True
        return False

    def just_place(self, piece, board, x, y):
        board[x, y] = piece
        piece.placed = True

    #TODO: Factorize
    def nb_edge_match(self, board):
        nb_match = 0
        for y in range(16):
            for x in range(16):
                if y > 0:
                    if board[x, y].upEdge == board[x, y - 1].downEdge:
                        nb_match += 1
                else:
                    if board[x, y].upEdge == PatternPieces.EDGE:
                        nb_match += 1
                if y < 15:
                    if board[x, y].downEdge == board[x, y + 1].upEdge:
                        nb_match += 1
                else:
                    if board[x, y].downEdge == PatternPieces.EDGE:
                        nb_match += 1
                if x > 0:
                    if board[x, y].leftEdge == board[x - 1, y].rightEdge:
                        nb_match += 1
                else:
                    if board[x, y].leftEdge == PatternPieces.EDGE:
                        nb_match += 1
                if x < 15:
                    if board[x, y].rightEdge == board[x, y].leftEdge:
                        nb_match += 1
                else:
                    if board[x, y].rightEdge == PatternPieces.EDGE:
                        nb_match += 1
        return nb_match


    def isGoalAchieved(self, board):
        for y in range(16):
            for x in range(16):
                if (board[x, y] is None):
                    return False

                # Checks above cell
                if (y != 0):
                    side = board[x, y - 1].getSidePattern(2)
                    if (side == False or side != board[x, y].getSidePattern(0)):
                        return False
                # Checks if top side is an edge
                else:
                    if (board[x, y].getSidePattern(0) != PatternPieces.EDGE):
                        return False

                # Checks next cell
                if (x != 15):
                    side = board[x + 1, y].getSidePattern(3)
                    if (side == False or side != board[x, y].getSidePattern(1)):
                        return False
                # Checks if right side is an edge
                else:
                    if (board[x, y].getSidePattern(1) != PatternPieces.EDGE):
                        return False

                # Checks below cell
                if (y != 15):
                    side = board[x, y + 1].getSidePattern(0)
                    if (side == False or side != board[x, y].getSidePattern(2)):
                        return False
                # Checks if bottom side is an edge
                else:
                    if (board[x, y].getSidePattern(2) != PatternPieces.EDGE):
                        return False

                # Checks previous cell
                if (x != 0):
                    side = board[x - 1, y].getSidePattern(1)
                    if (side == False or side != board[x, y].getSidePattern(3)):
                        return False
                # Checks if left side is an edge
                else:
                    if (board[x, y].getSidePattern(3) != PatternPieces.EDGE):
                        return False
        return True