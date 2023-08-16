board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

def play():
    player = 'X'
    while True:
        print_board()
        move = input('Player ' + player + ', enter a number (1-9): ')
        move = int(move) - 1
        if board[move] == ' ':
            board[move] = player
            if player_won(player):
                print_board()
                print('Player ' + player + ' won!')
                break
            elif board_full():
                print_board()
                print('Tie!')
                break
            else:
                player = 'O'
        else:
            print('Invalid move')

def player_won(player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

def board_full():
    for i in range(9):
        if board[i] == ' ':
            return False
    return True

play()
