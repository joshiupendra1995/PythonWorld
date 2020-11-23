theBoard = ['-', '-', '-',
            '-', '-', '-',
            '-', '-', '-']
current_player = 'X'
filled_board = True
valid_inputs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def play_game(board):
    print_board(theBoard)
    global filled_board
    global valid_inputs

    while filled_board:
        pos = input(f'enter your choice player "{current_player}" between 1-9 :: ')
        while pos not in valid_inputs or board[int(pos) - 1] != '-':
            pos = input(
                f'Invalid Input or position already filled!! please enter valid choice player "{current_player}" between 1-9 :: ')
        else:
            position = int(pos) - 1
        board[position] = current_player
        flip_player(current_player)

        if '-' not in theBoard:
            filled_board = False
        print_board(board)

        winner_result(board)


def flip_player(player):
    global current_player
    if player == 'O':
        current_player = 'X'
    elif player == 'X':
        current_player = 'O'


def winner_result(board):
    global filled_board
    winner = ''
    if board[0] != '-' and board[0] == board[1] == board[2]:
        winner = board[0]
    elif board[3] != '-' and board[3] == board[4] == board[5]:
        winner = board[3]
    elif board[6] != '-' and board[6] == board[7] == board[8]:
        winner = board[6]
    elif board[0] != '-' and board[0] == board[3] == board[6]:
        winner = board[0]
    elif board[1] != '-' and board[1] == board[4] == board[7]:
        winner = board[1]
    elif board[2] != '-' and board[2] == board[5] == board[8]:
        winner = board[2]
    elif board[0] != '-' and board[0] == board[4] == board[8]:
        winner = board[0]
    elif board[2] != '-' and board[2] == board[4] == board[6]:
        winner = board[2]
    if winner == '' and not filled_board:
        print("Game Over Its a tie!!")
        exit(1)
    elif winner != '' and filled_board:
        print(f'Game Over {winner} Wins!!')
        exit(1)


play_game(theBoard)
