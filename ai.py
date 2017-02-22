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
    def test(self, pb, app, arbiter, board):
        list_board = copy.deepcopy(board)

        list_board[13, 13] = pb.pieceslist[50]
        pb.pieceslist[50].nbofrightrotate = 2
        list_board[14, 13] = pb.pieceslist[55]
        pb.pieceslist[55].nbofrightrotate = 0

        print(arbiter.nb_edge_match(list_board))
        app.drawTable(list_board)


    def mutate_some_boards(self, pb, app, arbiter, boards, nb_mutate, nb_select):
        list_of_mutated = []

        for i in range (nb_mutate):
            rand = random.randint(0, nb_select)
            board = boards[rand]

            board_to_append = copy.deepcopy(board)
            for j in range (5):
                self.mutate_board_swap(board_to_append[0])
                self.mutate_swap_turn_tab(board_to_append[1])

            self.set_pieces_to_rot(board_to_append[1], pb)
            board_to_append[2] = arbiter.nb_edge_match(board_to_append[0])
            list_of_mutated.append(board_to_append)
        return list_of_mutated

    def create_random_boards(self, pb, app, arbiter, board, nb_boards):
        list_of_boards = []

        for i in range(nb_boards):
            board_c = copy.deepcopy(board)
            self.full_random_putting_pieces(pb, app, arbiter, board_c)

            rot = list()
            for j in range(0, 256):
                rot.append(board_c[int(j % 16), int(j / 16)].nbofrightrotate)
            self.set_pieces_to_rot(rot, pb)
            result = arbiter.nb_edge_match(board_c)

            list_board = copy.deepcopy(board_c)

            lists = [list_board, rot, result]
            list_of_boards.append(lists)
            self.reset_pieces(pb, app, arbiter, board_c)


        return list_of_boards


    def main_function(self, pb, app, arbiter, board):

        nb_boards = 100
        nb_selection = 10
        nb_mutation = 20

        list_of_random_boards = self.create_random_boards(pb, app, arbiter, board, nb_boards)
        list_of_random_boards.sort(key=operator.itemgetter(2), reverse=True)



        list_of_mutated_boards = self.mutate_some_boards(pb, app, arbiter, list_of_random_boards, nb_mutation, nb_selection)
        list_of_mutated_boards.sort(key=operator.itemgetter(2), reverse=True)


        print(list_of_mutated_boards[0])
        self.set_pieces_to_rot(list_of_mutated_boards[0][1], pb)
        app.drawTable(list_of_mutated_boards[0][0])

        # end of debug

        #end of crossover

        #mutation time

       #  list_of_mutated = []
        #for i in range(100):
        #    rand = random.randint(0, 10)
         #   boards = list_of_boards2_nd_gen[rand]
#
 #           board_to_append = copy.deepcopy(boards)
  #          for j in range (5):
   #             self.mutate_board_swap(board_to_append[0])
    #            self.mutate_swap_turn_tab(board_to_append[1])
#
 #           self.set_pieces_to_rot(board_to_append[1], pb)
  #          board_to_append[2] = arbiter.nb_edge_match(board_to_append[0])
   #         list_of_mutated.append(board_to_append)
        #end of mutation

     #   list_of_mutated.sort(key=operator.itemgetter(2), reverse=True)
        # debug prints


    def findPiece(self, piece, board):
        for x in range(256):
            if (board[int(x % 16), int(x / 16)].id == piece.id):
                    return (x)


    def mutate_board_swap(self, board):
        rand1 = random.randint(0, 255)
        rand2 = random.randint(0, 255)

        piece1 = board[int(rand1 % 16), int(rand1 / 16)]
        piece2 = board[int(rand2 % 16), int(rand2 / 16)]

        board[int(rand2 % 16), int(rand2 / 16)] = piece1
        board[int(rand1 % 16), int(rand1 / 16)] = piece2

    def set_pieces_to_rot(self, rot, pb):
        for i in range (256):
            pb.pieceslist[i].nbofrightrotate = rot[i]

    def mutate_swap_turn(self, board):
        rand = random.randint(0, 255)
        board[int(rand % 16), int(rand / 16)] = rand.randint(0, 3)

    def mutate_swap_turn_tab(self, rot):
        rand = random.randint(0, 255)
        rot[rand] = random.randint(0, 3)

    def osef_total_bullshit_i_dont_want_to_throw(self):

        list_of_boards2_nd_gen = []

        for i in range(100):
            mate1 = random.randint(0, 5)
            mate2 = random.randint(0, 4)

            new_board = copy.deepcopy(list_of_boards[mate1][0])
            self.set_pieces_to_rot(list_of_boards[mate1][1], pb)
            for j in range(256):
                if (random.randint(0, 1) == 1):  # Swaping for 2 pieces within the 2 puzzle
                    boardtmp = list_of_boards[mate2][0]
                    pos_piece1 = self.findPiece(boardtmp[int(j % 16), int(j / 16)], list_of_boards[mate1][0])

                    piece_tmp = new_board[int(j % 16), int(j / 16)]
                    rot_tmp = list_of_boards[mate1][1][j]

                    new_board[int(j % 16), int(j / 16)] = new_board[int(pos_piece1 % 16), int(pos_piece1 / 16)]
                    new_board[int(j % 16), int(j / 16)].nbofrightrotate = list_of_boards[mate2][1][pos_piece1]

                    new_board[int(pos_piece1 % 16), int(pos_piece1 / 16)] = piece_tmp
                    new_board[int(pos_piece1 % 16), int(pos_piece1 / 16)].nbofrightrotate = rot_tmp

            result = arbiter.nb_edge_match(new_board)
            rot = list()
            for j in range(0, 256):
                rot.append(new_board[int(j % 16), int(j / 16)].nbofrightrotate)
            lists = [new_board, rot, result]
            list_of_boards2_nd_gen.append(lists)

        list_of_boards2_nd_gen.sort(key=operator.itemgetter(2), reverse=True)
