
def print_board(board):
    for row in range(0, 3):
        for col in range(0, 3):
            print(board[row][col], end=' ') 
        print()


board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]
player = 'X'

while True:
    print(f'{player} plays')
    print_board(board)
    row = int(input("Row (1-3): ")) - 1
    col = int(input("Col (1-3): ")) - 1
    # if location is valid and if location available
    if row < 0 or row > 2 or col < 0 or col > 2:
        print(f'Invalid position {row} - {col}')
        continue
    if board[row][col] != '-':
        print(f'Position {row} - {col} already used')
        continue
    board[row][col] = player 
    player = 'X' if player=='O' else 'O'

    # Check for winner
    # Check for tie