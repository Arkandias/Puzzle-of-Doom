class Ai:
    def __init__(self):
        pass

    def test_putting_pieces(self, pb, app, arbiter, board):
        for y in range(16):
            for x in range(16):
                for piece in pb.pieceslist:
                    if piece.placed is False:
                        if arbiter.check_and_place(piece, board, x, y) is True:
                            app.placePiece(board[x, y], x, y)
                            app.update()
                            break
                # app.drawTable(board)