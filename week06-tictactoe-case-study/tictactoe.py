
class Player:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name 
        self.score = 0

    def __str__(self):
        return f"{self.name} ({self.symbol})" 
    
    def increase_score(self):
        self.score += 1
    

class Game:
    def __init__(self, name_x, name_o):
        self.board = []
        self.player_x = Player('X', name_x)
        self.player_o = Player('O', name_o)
        self.reset_game()

    def reset_game(self):
        """Starts a new game by initializing board and current player"""
        self.init_board()
        self.current_player = self.player_x

    def init_board(self):
        """Intitalizes to an empty board"""
        self.board = [
            ['-','-','-'],['-','-','-'],['-','-','-']
        ]

    def display_board(self):
        """Displays the board in rows and columns"""
        for r in range(3):
            for c in range(3):
                print(self.board[r][c], end=' ')
            print()

    def play(self, row, col):
        """
        Verify that row and col are valid within the range 1-3.
        Verify that the row-col cell is available.
        Allocate the row-col cell to the current player.
        Change player.
        """
        if row < 1 or row > 3 or col < 1 or col > 3:
            print("Invalid row or col")
            return
        row -= 1
        col -= 1
        if self.board[row][col] != '-':
            print("Position is already taken")
            return 
        self.board[row][col] = self.current_player.symbol
        if self.current_player == self.player_x:
            self.current_player = self.player_o
        else:
            self.current_player = self.player_x

    def check_winner(self):
        # Check every row
        for r in range(3):
            if self.board[r][0] == self.board[r][1] == self.board[r][2] and \
                self.board[r][0] != '-':
                return self.board[r][0]
        # Check every column
        for c in range(3):
            if self.board[0][c] == self.board[1][c] == self.board[2][c] and \
                self.board[0][c] != '-':
                return self.board[0][c]
        # Check right diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and \
                self.board[1][1] != '-':
                return self.board[1][1]
        # Check left diagonal
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and \
                self.board[1][1] != '-':
                return self.board[1][1]
        # No winner found above
        return None 
    
    def check_tie(self):
        """Scan the board and if a dash '-' is found assume no tie"""
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == '-':
                    return False 
        # loops completed, no '-' found, assume it's a tie
        return True 
    
    def update_score(self, winner): 
        if winner == 'X':
            self.player_x.increase_score()
        elif winner == 'O':
            self.player_o.increase_score()
        else:
            print("Invalid player")

    def save_score(self):
        """Write the score to the score file"""
        file = open('tictactoe_score.csv', 'a')
        row = f"{self.player_x.name},{self.player_o.name},{self.player_x.score},{self.player_o.score}\n"
        file.write(row)
        file.close()



name_x = input("Player X name: ")
name_o = input("Player O name: ")
game = Game(name_x, name_o)

play_again = 'y'

while play_again == 'y':
    game.display_board()
    print(f"{game.current_player} plays:")
    row = int(input("Give Row (1-3): "))
    col = int(input("Give Col (1-3): "))
    game.play(row, col)
    winner = game.check_winner()
    if winner is not None:
        game.display_board()
        print(f"Winner {game.check_winner()}")
        game.update_score(winner)
    tie = False 
    if winner is None:
        tie = game.check_tie()
        if tie:
            game.display_board()
            print("It's a Tie")
    if winner is not None or tie: 
        play_again = input("Play again y/n? ")
        if play_again == 'y':
            game.reset_game()


game.save_score()

print("Bye!")

