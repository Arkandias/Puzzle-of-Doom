import random
import copy
import operator

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
                #app.placePiece(board[x, y], x, y)
                #app.update()
                #break
                    # app.drawTable(board)


    def main_function(self, pb, app, arbiter, board):
        boards = list()

        res = int()
        list_of_boards = []

        for i in range (100):
            self.full_random_putting_pieces(pb, app, arbiter, board)
            result = arbiter.nb_edge_match(board)
            rot = list()
            for j in range(0,256):
                rot.append(board[int(j % 16), int(j / 16)].nbofrightrotate)

            list_board = copy.deepcopy(board)

            lists = [list_board, rot, result]
            list_of_boards.append(lists)
            self.reset_pieces(pb, app, arbiter, board)



        list_of_boards.sort(key=operator.itemgetter(2), reverse=True)

        list_of_boards2_nd_gen = []

        for i in range(100):
            mate1 = random.randint(0, 5)
            mate2 = random.randint(0, 4)

            new_board = copy.deepcopy(list_of_boards[mate1][0])

            for j in range(256):
                if (random.randint(0, 1) == 1):
                    boardtmp = list_of_boards[mate2][0]
                    pos_piece1 = self.findPiece(boardtmp[int(j % 16), int(j / 16)], list_of_boards[mate1][0])

                    piece_tmp = new_board[int(j % 16), int(j / 16)]
                    new_board[int(j % 16), int(j / 16)] = new_board[int(pos_piece1 % 16), int(pos_piece1 / 16)]
                    new_board[int(pos_piece1 % 16), int(pos_piece1 / 16)] = piece_tmp

                    #new_board[int(j % 16), int(j / 16)] = list_of_boards[mate2][0][int(j % 16), int(j / 16)]
                    #new_board[int(j % 16), int(j / 16)].nbofrightrotate = list_of_boards[mate2][1][(j % 16) + (j * 16)]
            result = arbiter.nb_edge_match(new_board)
            rot = list()
            for j in range(0, 256):
                rot.append(new_board[int(j % 16), int(j / 16)].nbofrightrotate)
            lists = [new_board, rot, result]
            list_of_boards2_nd_gen.append(lists)

        list_of_boards2_nd_gen.sort(key=operator.itemgetter(2), reverse=True)

        app.drawTable(list_of_boards2_nd_gen[0][0])

    def findPiece(self, piece, board):
        for x in range(256):
            if (board[int(x % 16), int(x / 16)].id == piece.id):
                    return (x)