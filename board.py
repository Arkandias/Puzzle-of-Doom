class Board:
    def __init__(self):
        self.board = [None] * 256
    
    def __getitem__(self, key):
        return self.board[key[0] + key[1] * 16]

    def __setitem__(self, key, value):
        value.position['x'] = key[0]
        value.position['y'] = key[1]
        self.board[key[0] + key[1] * 16] = value

    def __delitem__(self, key):
        if (self.board[key[0] + key[1] * 16] is not None):
            self.board[key[0] + key[1] * 16].position = {'x': None, 'y': None}
        self.board[key[0] + key[1] * 16] = None

    def getEmptyCells(self):
        cells = []
        for x in range(len(self.board)):
            if (self.board[x] == None):
                cells.append(x)
        return cells

    def getOccupiedCells(self):
        cells = []
        for x in range(len(self.board)):
            if (self.board[x] != None):
                cells.append(x)
        return cells
