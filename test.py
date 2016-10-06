import unittest
from main import draw_board, check_horizontal, check_vector


class TestDrawBoard(unittest.TestCase):
    def test_3x3_board(self):
        edge_size = 3
        board_size = edge_size * edge_size
        board = list(range(1, board_size + 1))
        output = draw_board(board, edge_size)
        board_3x3 = '  1  |  2  |  3  \n-----------------\n'
        board_3x3 += '  4  |  5  |  6  \n-----------------\n'
        board_3x3 += '  7  |  8  |  9  '
        self.assertEqual(output, board_3x3)

    def test_4x4_board(self):
        edge_size = 4
        board_size = edge_size * edge_size
        board = list(range(1, board_size + 1))
        output = draw_board(board, edge_size)
        board_4x4 = '  1  |  2  |  3  |  4  \n-----------------------\n'
        board_4x4 += '  5  |  6  |  7  |  8  \n-----------------------\n'
        board_4x4 += '  9  | 10  | 11  | 12  \n-----------------------\n'
        board_4x4 += ' 13  | 14  | 15  | 16  '
        self.assertEqual(output, board_4x4)


class TestCheckVector(unittest.TestCase):
    def test_small_vectors(self):
        self.assertFalse(check_vector([], 'X'), 'check_vector should return False with an emtpy vector')
        self.assertFalse(check_vector(['X'], 'X'), 'check_vector should return False with a vector of 1 element')
        self.assertFalse(check_vector(['X', 'X'], 'X'), 'check_vector should return False with a vector of 2 element')

    def test_bad_marker(self):
        with self.assertRaises(AssertionError):
            check_vector(['X', 'X', 'O'], 'Z')

    def test_bad_vectors(self):
        self.assertFalse(check_vector(['X', 'O', 'X'], 'X'))
        self.assertFalse(check_vector(['X', 'X', 'O', 'X'], 'X'))
        self.assertFalse(check_vector(['O', 'O', 'X', 'O', 'O'], 'O'))

    def test_good_vectors(self):
        self.assertTrue(check_vector(['X', 'X', 'X'], 'X'))
        self.assertTrue(check_vector(['O', 'O', 'O'], 'O'))
        self.assertTrue(check_vector(['O', 'O', 'O', 'X', 'X'], 'O'))
        self.assertTrue(check_vector(['X', 'X', 'O', 'O', 'O'], 'O'))
        self.assertTrue(check_vector(['X', 'O', 'O', 'O', 'X'], 'O'))


class TestCheckHorizontal(unittest.TestCase):
    def test_3x3(self):
        edge_size = 3
        board_size = edge_size * edge_size
        board = list(range(1, board_size + 1))
        for box in range(3):
            self.assertEqual(check_horizontal(board, box=box, row=0, edge_size=edge_size), [1, 2, 3])
        for box in range(3, 6):
            self.assertEqual(check_horizontal(board, box=box, row=1, edge_size=edge_size), [4, 5, 6])
        for box in range(6, 9):
            self.assertEqual(check_horizontal(board, box=box, row=2, edge_size=edge_size), [7, 8, 9])

    def test_8x8(self):
        edge_size = 8
        board_size = edge_size * edge_size
        board = list(range(1, board_size + 1))
        self.assertEqual(check_horizontal(board, box=0, row=0, edge_size=edge_size), [1, 2, 3])
        self.assertEqual(check_horizontal(board, box=1, row=0, edge_size=edge_size), [1, 2, 3, 4])
        self.assertEqual(check_horizontal(board, box=2, row=0, edge_size=edge_size), [1, 2, 3, 4, 5])
        self.assertEqual(check_horizontal(board, box=3, row=0, edge_size=edge_size), [2, 3, 4, 5, 6])
        self.assertEqual(check_horizontal(board, box=4, row=0, edge_size=edge_size), [3, 4, 5, 6, 7])
        self.assertEqual(check_horizontal(board, box=5, row=0, edge_size=edge_size), [4, 5, 6, 7, 8])
        self.assertEqual(check_horizontal(board, box=6, row=0, edge_size=edge_size), [5, 6, 7, 8])
        self.assertEqual(check_horizontal(board, box=7, row=0, edge_size=edge_size), [6, 7, 8])


if __name__ == '__main__':
    unittest.main()
