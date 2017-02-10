class Ai:
    def __init__(self):
        pass

    def test_putting_pieces(self, pb, app, arbiter, board):
        for y in range(0, 14):
            print(y)
            for x in range(0, 17):
                for piece in pb.pieceslist:
                    if piece.placed is False:
                        if arbiter.check_and_place(piece, board, x, y) is True:
                            break
                app.drawTable(board)