class Board:
    def __init__(self):
        self.board = [[None] * 16] * 16
    
    def __getitem__(self, key):
        return self.board[key[0]][key[1]]

    def __setitem__(self, key, value):
        value.position['x'] = key[0]
        value.position['y'] = key[1]
        self.board[key[0]][key[1]] = value

    def __delitem__(self, key):
        value.position['x'] = None
        value.position['y'] = None
        self.board[key[0]][key[1]] = None