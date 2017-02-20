import random

class Ai:
    def __init__(self):
        pass

    def test_putting_pieces(self, pb, app, arbiter, board):
        for y in range(16):
            for x in range(16):
                for piece in pb.pieceslist:
                    if piece.placed is False:
                        arbiter.just_place(piece, board, x, y)
                        app.placePiece(board[x, y], x, y)
                        app.update()
                        break
                # app.drawTable(board)

    def reset_pieces(self, pb, app, arbiter, board):
        for i in range(256):
            pb.pieceslist[i].nbofrightrotate = 0
            pb.pieceslist[i].placed = False

    def full_random_putting_pieces(self, pb, app, arbiter, board):
        for y in range(16):
            for x in range(16):
                unplaced_pieces = 1
                #while unplaced_pieces != 0:
                list_no_placed = [x for x in pb.pieceslist if x.placed is False]
                #unplacedList = filter (lambda : pb.pieceslist.placed == False, pb.pieceslist)
                unplaced_pieces = len(list_no_placed)
                if (unplaced_pieces == 0):
                    return
                if (unplaced_pieces == 1):
                    piecesnb = 0
                else:
                    piecesnb = random.randint(0, unplaced_pieces - 1)
                rot = random.randint(0, 3)
                list_no_placed[piecesnb].nbofrightrotate = rot
                arbiter.just_place(list_no_placed[piecesnb], board, x, y)
                app.placePiece(board[x, y], x, y)
                app.update()
                #break
                    # app.drawTable(board)


    def main_function(self, pb, app, arbiter, board):
        for i in range (100):
            self.full_random_putting_pieces(pb, app, arbiter, board)
            print(arbiter.nb_edge_match(board))
            self.reset_pieces(pb, app, arbiter, board)