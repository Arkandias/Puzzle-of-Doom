import random
import copy
import operator
import json
import os
import csv
from board import Board

from board import Board

class Ai:

    def __init__(self):
        self.placedPieces = []
        self.unplacedPieces = []
        self.gennumber = 0
        self.board = Board()

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

    def crossover(self, pb, app, board, arbiter, list_of_random_boards, nb_fitness, nb_tab, nb_selection):
        list_of_crossover = []

        for i in range (nb_tab):
            rand1 = random.randint(0, nb_selection)
            rand2 = random.randint(0, nb_selection - 1)

            if (rand1 == rand2):
                rand2 = rand2 + 1

            self.set_pieces_to_rot(list_of_random_boards[rand1][1], pb)
            list1 = self.best_fitnet_board(arbiter, list_of_random_boards[rand1][0], nb_fitness)

            self.set_pieces_to_rot(list_of_random_boards[rand2][1], pb)
            list2 = self.best_fitnet_board(arbiter, list_of_random_boards[rand2][0], nb_fitness)

            rot_son = []
            board_son = Board()
            for i in range (256):
                pb.pieceslist[i].placed = False
                #board_son[int(i % 16), int(i / 16)] = None
                rot_son.append(0)

            board1 = list_of_random_boards[rand1][0]
            rot1 = list_of_random_boards[rand1][1]
            for i in range (nb_fitness):
                x = int(list1[i][0] % 16)
                y = int(list1[i][0] / 16)
                if (board1[x, y].placed == False):
                    board_son[x, y] = board1[x, y]
                    board_son[x, y].placed = True
                    rot_son[int(x % 16 + y * 16)] = rot1[int(x % 16 + y * 16)]



            board2 = list_of_random_boards[rand2][0]
            rot2 = list_of_random_boards[rand2][1]
            for i in range (256):
                x = int(list2[i][0] % 16)
                y = int(list2[i][0] / 16)
                if (board_son[x, y] is None):
                    if (board2[x, y].placed == False):
                        board_son[x, y] = board2[x, y]
                        board_son[x, y].placed = True
                        rot_son[int(x % 16 + y * 16)] = rot2[int(x % 16 + y * 16)]


            nb_lel = 0
            tag = 1
            for i in range (256):
                if (board_son[i % 16, int(i/16)] is None):
                    nb_lel += 1
                    list_no_placed = [x for x in pb.pieceslist if x.placed is False]
                    unplaced_pieces = len(list_no_placed)
                    if (unplaced_pieces == 0):
                        print("that was not suppose to happen")
                        tag = 0
                        if (tag == 0):
                            for k in range(256):
                                print(pb.pieceslist[k].placed)
                        continue
                    if (unplaced_pieces == 1):
                        piecesnb = 0
                    else:
                        piecesnb = random.randint(0, unplaced_pieces - 1)
                    rot = random.randint(0, 3)
                    board_son[i % 16, int(i / 16)] = list_no_placed[piecesnb]
                    board_son[i % 16, int(i / 16)].placed = True
                    rot_son[i] = rot


            self.set_pieces_to_rot(rot_son, pb)


            list_of_crossover.append([board_son, rot_son, arbiter.nb_edge_match(board_son)])
        return list_of_crossover


    def best_fitnet_board(self, arbiter, board, nb_best):
        list_of_best = []
        for i in range(256):
            list_of_best.append([i, arbiter.nb_edge_piece(board, i % 16, int(i / 16))])
        list_of_best.sort(key=operator.itemgetter(1), reverse=True)
        list_of_best[:nb_best]



        return list_of_best

    def change_board_to_id(self, board):
        x_tab = []
        for x in range(16):
            y_tab = []
            for y in range(16):
                if (board[x, y] is not None):
                    y_tab.append(board[x, y].id)
                else:
                    y_tab.append(0)
            x_tab.append(y_tab)
        return x_tab

    def change_id_to_board(self, id, pb):
        board = Board()
        for x in range(16):
            for y in range(16):
                if (id[x][y] == 0):
                    board[x, y] = pb.pieceslist[0]
                else:
                    board[x, y] = pb.pieceslist[id[x][y] - 1]
        return board

    def save_result_only(self, gen, result):
        if os.path.isfile("./results.csv") is True:
            flag = 'a'
        else:
            flag = 'w'
        with open("./results.csv", flag) as csvfile:
            logwriter = csv.writer(csvfile)
            logwriter.writerow([gen, result])

    def load_gen_max(self):
        last_gen = 0
        if os.path.isfile("./results.csv") is True:
            with open("./results.csv", 'r') as csvfile:
                logreader = csv.reader(csvfile)
                for row in logreader:
                    if len(row) > 0:
                        last_gen = int(row[0])
        return last_gen

    def save(self, list_of_best):
        saved_list = copy.deepcopy(list_of_best)
        for nb, elem in enumerate(saved_list):
            board_to_list = self.change_board_to_id(elem[0])
            saved_list[nb][0] = board_to_list
        with open("./logs/" + str(len(os.listdir("./logs/"))) + ".txt", 'w') as jsonfile:
            json.dump(saved_list, jsonfile)

    def load_last_log(self, pb):
        if len(os.listdir("./logs/")) > 0:
            with open("./logs/" + str(len(os.listdir("./logs/")) - 1) + ".txt", 'r') as jsonfile:
                loaded_list = json.load(jsonfile)
            for nb, elem in enumerate(loaded_list):
                board_to_object = self.change_id_to_board(elem[0], pb)
                loaded_list[nb][0] = board_to_object
            return loaded_list
        else:
            return None

    def mutate_some_boards(self, pb, app, arbiter, boards, nb_mutate, nb_select, mutation):
        list_of_mutated = []

        for i in range (nb_mutate):
            rand = random.randint(0, nb_select)
            board = boards[rand]

            board_to_append = copy.deepcopy(board)



            for j in range (int ( mutation * 256 / 100)):
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


    def main_function(self, pb, app, arbiter, board, loop, fitness, mutation):
        nb_boards = 100
        nb_selection = 10
        nb_mutation = 100
        nb_fitness = int (256 * fitness / 100)
        nb_tab = 100
        nb_very_best_value_save = 3
        save_every_x_gen = 20

        print (mutation * 256 / 100)

        list_of_random_boards = []
        to_load = self.load_last_log(pb)
        if (to_load is None):
            list_of_random_boards = self.create_random_boards(pb, app, arbiter, board, nb_boards)
            list_of_random_boards.sort(key=operator.itemgetter(2), reverse=True)
        else:
            list_of_random_boards = to_load


        gen = self.load_gen_max()

        for j in range(loop):
            gen += 1
            list_of_crossover_boards = self.crossover(pb, app, board, arbiter, list_of_random_boards, nb_fitness,
                                                      nb_tab, nb_selection)
            list_of_crossover_boards.sort(key=operator.itemgetter(2), reverse=True)

            self.set_pieces_to_rot(list_of_crossover_boards[0][1], pb)
            app.drawTable(list_of_crossover_boards[0][0])
            app.update()
            # print(list_of_crossover_boards[0][2])

            list_of_mutated_boards = self.mutate_some_boards(pb, app, arbiter, list_of_crossover_boards, nb_mutation,
                                                             nb_selection, mutation)
            list_of_mutated_boards.sort(key=operator.itemgetter(2), reverse=True)

            self.set_pieces_to_rot(list_of_mutated_boards[0][1], pb)
            app.drawTable(list_of_mutated_boards[0][0])
            app.update()
            # print(list_of_mutated_boards[0][2])

            best_of_lists = []
            for i in range(nb_very_best_value_save):
                best_of_lists.append(list_of_random_boards[i])
            for i in range(nb_tab):
                best_of_lists.append(list_of_crossover_boards[i])
            for i in range(nb_mutation):
                best_of_lists.append(list_of_mutated_boards[i])
            best_of_lists.sort(key=operator.itemgetter(2), reverse=True)
            best_of_lists[:nb_boards]

            self.set_pieces_to_rot(best_of_lists[0][1], pb)
            app.drawTable(best_of_lists[0][0])
            app.update()
            print("Best score: " + str(best_of_lists[0][2]) + " at the gen n:" + str(gen))
            for i in range(9):
                print(str(i + 1) + " best score: " + str(best_of_lists[i + 1][2]) + " at the gen n:" + str(gen))

            list_of_random_boards = best_of_lists

            self.save_result_only(gen, best_of_lists[0][2])
            if ((gen % save_every_x_gen) == 0):
                self.save(best_of_lists)
            # end of debug

            # end of crossover

            # mutation time

            #  list_of_mutated = []
            # for i in range(100):
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
            # end of mutation

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