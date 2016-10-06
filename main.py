
def draw_board(board, edge_size):
    """
    Display the board in the console
    (A bit of overhead here but it makes the matrix scale nicely whatever size is)
    :param board: state of the current game
    :type board: list
    :param edge_size: edge size of the game board
    :type edge_size: int
    :return: board display
    """
    board_size = edge_size*edge_size
    output = ''
    for offset in range(0, board_size, edge_size):
        row = ''
        for i, item in enumerate(board[offset:offset+edge_size]):
            row += '{0:^5}{1}'.format(item, '|' if i < edge_size-1 else '')
        # we don't want to print the horizontal separator for last row
        if offset < board_size-edge_size:
            row += '\n' + '-'*len(row) + '\n'
        output += row
    return output


def check_vector(vector, marker):
    """
    Check if vector contains a sequence of 3 consecutive markers
    :param vector: a list of markers
    :type vector: list
    :param marker: enum char 'X' or 'O'
    :type marker: str
    :return: True if 3 consecutive markers are found
    """
    assert marker in ['X', 'O'], "Marker should be either 'X' or 'O' but found {0}".format(marker)
    if len(vector) < 3:
        return False
    else:
        i = 0
        while i+3 < len(vector)+1:
            if vector[i:i+3] == [marker]*3:
                return True
            i += 1
        return False


def check_horizontal(board, box, row, edge_size):
    """
    Extract an horizontal vector base on the box value and board boundaries
    :param board: state of the current game
    :type board: list
    :param box: last user move (or any other)
    :type box: int
    :param row: row index
    :type row: int
    :param edge_size: edge size of the game board
    :type edge_size: int
    :return: list of boxes
    """
    return board[max(row*edge_size, box-2):min((row+1)*edge_size, box+3)]


def check_vertical(board, box, row, edge_size):
    """
    Extract a vertical vector base on the box value and board boundaries
    :param board: state of the current game
    :type board: list
    :param box: last user move (or any other)
    :type box: int
    :param edge_size: edge size of the game board
    :return: list of boxes
    """
    # I probably should have rotate the matrix and reuse check_horizontal instead -_-'
    start = box - row * edge_size if row < 2 else box - 2 * edge_size
    end = box + (edge_size-(row+1)) * edge_size if row+1 > (edge_size-2) else box + 2 * edge_size
    return [board[index] for index in range(start, end+1, edge_size)]

# def check_diagonal():
#     """
#     Extract a diagonals vector base on the box value and board boundaries
#     :param board: state of the current game
#     :type board: list
#     :param box: last user move (or any other)
#     :type box: int
#     :param row: row index
#     :type row: int
#     :param edge_size: edge size of the game board
#     :return: list of boxes
#     """
#     pass


def check_result(board, edge_size, box, marker):
    """
    Check the game state after the last move
    :param board: state of the current game
    :type board: list
    :param edge_size: edge size of the game board
    :type edge_size: int
    :param box: last user move (or any other)
    :type box: int
    :param marker: enum char 'X' or 'O'
    :type marker: str
    :return:
    """
    box -= 1
    row = box // edge_size
    # col = box - row * edge_size

    if check_vector(check_horizontal(board, box, row, edge_size), marker):
        return True
    elif check_vector(check_vertical(board, box, row, edge_size), marker):
        return True
    # elif check_diagonal():
    #     return True
    else:
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
    print(draw_board(board, edge_size))
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
                print(draw_board(board, edge_size))
                if check_result(board, edge_size, box, markers[player]):
                    print('Congratulations {0}! You have won.'.format(players[player]))
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
    # TODO input N (minimum 2)
    # TODO add assert and test param imput
    # players = ['John', 'Paul'] # TODO set to []
    # player = 1
    # while player < 3:
    #     print('Enter name for Player {0}: '.format(player))
    #     name = input('>> ')
    #     if name:
    #         players.append(name)
    #         player += 1

    game(['John', 'Paul'], 4)
