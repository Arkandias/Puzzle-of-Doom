class Board:
    def __init__(self):
        self.board = [[None] * 16] * 16
    
    def __getitem__(self, key):
        return self.board[key[0]][key[1]]

    def __setitem__(self, key, value):
        self.board[key[0]][key[1]] = value

    def __delitem__(self, key):
        self.board[key[0]][key[1]] = None