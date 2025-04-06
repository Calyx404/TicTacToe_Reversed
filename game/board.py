x = '''
 --------------   --------------   --------------   --------------   --------------
|               |                |                |                |                |
|               |                |                |                |                |
|               |                |                |                |                |
 --------------   --------------   --------------   --------------   --------------
|               |                |                |                |                |
|               |                |                |                |                |
|               |                |                |                |                |
 --------------   --------------   --------------   --------------   --------------
|               |                |                |                |                |
|               |                |                |                |                |
|               |                |                |                |                |
 --------------   --------------   --------------   --------------   --------------
|               |                |                |                |                |
|               |                |                |                |                |
|               |                |                |                |                |
 --------------   --------------   --------------   --------------   --------------
|               |                |                |                |                |
|               |                |                |                |                |
|               |                |                |                |                |
 --------------   --------------   --------------   --------------   --------------
'''

class Board:
    def __init__(self, size:int, player:list=[], opponent:list=[]):
        self.size = size
        self.board = [[col + (size * row) for col in range(1, size + 1)] for row in range(size)]
        self.player = player
        self.opponent = opponent

    def display(self):
        cell_width = 15
        cell_height =  3

        break_line = (" " + "-" * cell_width) * self.size

        if len(self.player) != 0:
            for row in self.board:
                for tile in self.player:
                    if tile in row:
                        cell = row.index(tile)
                        row[cell] = 'X'

        if len(self.opponent) != 0:
            for row in self.board:
                for tile in self.opponent:
                    if tile in row:
                        cell = row.index(tile)
                        row[cell] = 'O'

        for row in self.board:
            print(break_line)
            for h in range(cell_height):
                if h == cell_height // 2:
                    print("".join(f"|{str(num).center(cell_width)}" for num in row) + "|")
                else:
                    print(("|" + " " * cell_width) * self.size + "|")
        print(break_line)

    def reset(self):
        self.player.clear()
        self.opponent.clear()
        self.board = [[col + (self.size * row) for col in range(1, self.size + 1)] for row in range(self.size)]
