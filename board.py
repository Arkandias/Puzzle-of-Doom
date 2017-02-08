class Board:
    def __init__(self):
        self.board = [None] * 256
    
    def __getitem__(self, key):
        return self.board[key[0] + key[1] * 16]

    def __setitem__(self, key, value):
        print(key)
        value.position['x'] = key[0]
        value.position['y'] = key[1]
        self.board[key[0] + key[1] * 16] = value

    def __delitem__(self, key):
        value.position['x'] = None
        value.position['y'] = None
        self.board[key[0] + key[1] * 16] = None