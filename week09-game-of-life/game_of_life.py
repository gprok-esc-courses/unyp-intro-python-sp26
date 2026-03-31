import random

class GameOfLife:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.board = []
        self.generation = 1
        self.init_board()
        

    def init_board(self):
        for r in range(self.height):
            row = []
            for c in range(self.width):
                row.append(random.randint(0, 1))
            self.board.append(row)
        self.generation = 1

    def display_board(self):
        print(f"GENERATION {self.generation}")
        for r in range(self.height):
            for c in range(self.width):
                print('X ' if self.board[r][c] == 1 else '- ', end='')
            print()

    def display_neighbors(self):
        for r in range(self.height):
            for c in range(self.width):
                print(self.get_alive_neigbours(r, c), end=' ')
            print()

    def get_alive_neigbours(self, r, c):
        total = 0
        for row in range(r - 1, r + 2):
            for col in range(c - 1, c + 2):
                if row >= 0 and col >= 0 and row < self.height and col < self.width:
                    total += self.board[row][col]
        total -= self.board[r][c]
        return total
    
    def calculate_next_gen(self):
        pass

gol = GameOfLife(5, 5)
gol.display_board()
gol.display_neighbors()

