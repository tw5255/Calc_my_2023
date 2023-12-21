def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]

    for condition in win_conditions:
        if all(cell == player for cell in condition):
            return True
    return False

def log_move(log_file, player, row, col):
    log_file.write(f"Player {player} made a move at ({row}, {col})\n")

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    log_file = open('game_log.txt', 'w')

    while True:
        print_board(board)
        try:
            row = int(input("Enter the row: "))
            col = int(input("Enter the column: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if row < 0 or row >= 3 or col < 0 or col >= 3:
            print("Invalid move. Try again.")
            continue

        if board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player
        log_move(log_file, current_player, row, col)

        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if all(cell != ' ' for row in board for cell in row):
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

    log_file.close()

play_game()