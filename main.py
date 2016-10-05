
def draw_board(board, edge_size):
    """
    Display the board in the console
    (A bit of overhead here but it makes the matrix scale nicely whatever size is)
    :param board: state of the current game
    :type board: list
    :param edge_size:
    :param edge_size: edge size of the game board
    :return: IO
    """
    board_size = edge_size*edge_size
    for offset in range(0, board_size, edge_size):
        row = ''
        for i, item in enumerate(board[offset:offset+edge_size]):
            row += '{0:^5}{1}'.format(item, '|' if i < edge_size-1 else '')
        print(row)
        # we don't want to print the horizontal separator for last row
        if offset < board_size-edge_size:
            print('-'*len(row))

def check_result(board, player_name):
    """
    Check the game state after the last move
    :param board: state of the current game
    :type board: list
    :param player_name: name of the player who did the last move
    :type player_name: str
    :return:
    """
    # print('Congratulations {0}! You have won.'.format(player_name))
    return False

def game(players, edge_size):
    """
    Start the game
    :param players: players list
    :type players: list
    :param edge_size:
    :param edge_size: edge size of the game board
    :return:
    """
    markers = ['X', 'O']
    board_size = edge_size*edge_size
    board = list(range(1, board_size + 1))
    draw_board(board, edge_size)
    player = 0
    moves = 0
    while True:
        print('{0}, choose a box to place an \'{1}\' into:'.format(players[player], markers[player]))
        box = input('>> ')
        if box.isnumeric():
            box = int(box)
            if isinstance(board[box-1], int):
                moves += 1
                board[box-1] = markers[player]
                draw_board(board, edge_size)
                if check_result(board, players[player]):
                    break
                if moves == board_size:
                    print('Sorry guys but that\'s a draw')
                    break
                else:
                    player = int(not player)
            else:
                print('This box is already played, please select a new one')
        else:
            print('Please enter a number between 1 and {0}'.format(board_size))




if __name__ == '__main__':
    players = ['John', 'Paul'] # TODO set to []
    player = 1
    # while player < 3:
    #     print('Enter name for Player {0}: '.format(player))
    #     name = input('>> ')
    #     if name:
    #         players.append(name)
    #         player += 1

    game(players, 3)
