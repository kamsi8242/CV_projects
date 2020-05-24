# This python file is dedicated to making a game of noughts and crosses
def tictacttoe():
    # Import modules
    import numpy as np

    # Welcome players to the game
    print('Welcome to my game of Tic-Tac-Toe')
    # first I need to make the three by three game board
    board = [[0, 0, 0, ], [0, 0, 0, ], [0, 0, 0, ]]
    board_matrix = np.array(board)
    print(board_matrix[:])

    print('\n'
          'How to play the game: The board is made of a  3*3 matrix, to select the position to place your counter(s) '
          'first enter the row number followed by the column number. Remember a matrix starts from 0 not 1, '
          'so the range of inputs should be between 0 and 2.')

    # Couldn't use this in my matrix, so stuck to using integers
    # cross = 1
    # nought = 4

    while np.count_nonzero(board_matrix) < 9:
        p_row = int(input('Enter the row you want to place a marker: '))  # Enter player row
        p_col = int(input('Enter the column you want to place a marker: '))  # Enter player column
        # Prevents wrong inputs from crashing the game
        if p_row not in range(0, 3) or p_col not in range(0, 3):
            print('Invalid location \n'
                  'Rows and columns are between 0 and 2')
        # Tells players if there is already a counter in that location
        elif board_matrix[p_row][p_col] != 0:
            print('\n'
                  'There is already a counter there, choose another location')
        # Allows counters to be placed in valid locations
        elif board_matrix[p_row][p_col] == 0:
            counter = int(input('Enter your counter; p1: 1 p2: 4 \n'))
            board_matrix[p_row][p_col] = counter
            print(board_matrix)

        # Diagonal win conditions
        if (board_matrix[0, 0] + board_matrix[1, 1] + board_matrix[2, 2]) == 3 \
                or (board_matrix[0, 2] + board_matrix[1, 1] + board_matrix[2, 0]) == 3:
            print('Player 1 is the winner!!')
            break
        elif (board_matrix[0, 0] + board_matrix[1, 1] + board_matrix[2, 2]) == 12 \
                or (board_matrix[0, 2] + board_matrix[1, 1] + board_matrix[2, 0]) == 12:
            print('Player 2 is the winner!!')
            break
        # Horizontal and vertical win conditions
        elif sum(board_matrix[0, :]) == 3 or sum(board_matrix[1, :]) == 3 or sum(board_matrix[2, :]) == 3 or \
                sum(board_matrix[:, 0]) == 3 or sum(board_matrix[:, 1]) == 3 or sum(board_matrix[:, 2]) == 3:
            print('Player 1 is the Winner!!')
            break
        elif sum(board_matrix[0, :]) == 12 or sum(board_matrix[1, :]) == 12 or sum(board_matrix[2, :]) == 12 or \
                sum(board_matrix[:, 0]) == 12 or sum(board_matrix[:, 1]) == 12 or sum(board_matrix[:, 2]) == 12:
            print('Player 2 is the Winner!!')
            break
        # Drawing condition
        elif np.sum(board_matrix[:]) == 21:
            print('Draw!')
        continue

    # Offers players a chance to replay the game
    replay = str(input('Game Over, play again? (Y/N): ')).upper()
    if replay == 'Y':
        tictacttoe()


tictacttoe()
