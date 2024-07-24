import unittest
from tic_tac_toe_Andy_Chen import TicTacToe

class TestTicTacToeWins(unittest.TestCase):

    def test_check_winner_horizontal_X(self):
        board = [
            ["X", "X", "X", "X"],
            [None, "O", "O", None],
            [None, None, None, None],
            [None, None, None, None]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.check_winner(), "X")

    def test_check_winner_horizontal_O(self):
        board = [
            [None, "X", "X", None],
            [None, None, None, None],
            [None, None, None, None],
            ["O", "O", "O", "O"]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.check_winner(), "O")

    def test_check_winner_vertical_X(self):
        board = [
            ["X", None, None, None],
            ["X", "O", "O", None],
            ["X", None, None, None],
            ["X", None, None, None]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.check_winner(), "X")

    def test_check_winner_vertical_O(self):
        board = [
            ["X", None, "O", None],
            ["O", "O", "O", None],
            ["X", None, "O", None],
            ["X", None, "O", None]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.check_winner(), "O")
    
    def test_check_winner_diagonal_X(self):
        board = [
            ["X", None, None, None],
            [None, "X", None, None],
            [None, None, "X", None],
            [None, None, None, "X"]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.check_winner(), "X")

    def test_check_winner_diagonal_O(self):
        board = [
            ["O", None, None, None],
            [None, "O", None, None],
            [None, None, "O", None],
            [None, None, None, "O"]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.check_winner(), "O")
    
    def test_check_winner_anti_diagonal_X(self):
        board = [
            [None, None, None, "X"],
            [None, None, "X", None],
            [None, "X", None, None],
            ["X", None, None, None]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.check_winner(), "X")
    
    def test_check_winner_anti_diagonal_O(self):
        board = [
            [None, None, None, "O"],
            [None, None, "O", None],
            [None, "O", None, None],
            ["O", None, None, None]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.check_winner(), "O")
    
    def test_check_winner_corner_2x2_box_X(self):
        board = [
            ["X", "X", None, None],
            ["X", "X", "O", None],
            [None, "O", None, None],
            [None, None, None, None]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.check_winner(), "X")
    
    def test_check_winner_corner_2x2_box_O(self):
        board = [
            ["X", "X", None, None],
            ["O", "X", "O", "X"],
            [None, "X", "O", "O"],
            [None, None, "O", "O"]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.check_winner(), "O")
    
    def test_check_winner_inner_2x2_box_X(self):
        board = [
            ["O", "X", "X", None],
            ["O", "X", "X", None],
            [None, "O", None, None],
            [None, None, None, None]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.check_winner(), "X")

    def test_check_winner_inner_2x2_box_O(self):
        board = [
            ["O", "X", "X", None],
            ["O", "O", "X", None],
            ["O", "O", None, None],
            ["X", None, None, None]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.check_winner(), "O")
    
    def test_check_winner_four_corners_X(self):
        board = [
            ["X", None, None, "X"],
            [None, None, None, None],
            [None, None, None, None],
            ["X", None, None, "X"]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.check_winner(), "X")

    def test_check_winner_four_corners_O(self):
        board = [
            ["O", None, None, "O"],
            [None, None, None, None],
            [None, None, None, None],
            ["O", None, None, "O"]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.check_winner(), "O")

    def test_check_winner_no_winners(self):
        board = [
            ["O", None, None, "X"],
            [None, None, None, None],
            [None, None, None, None],
            ["X", None, None, "X"]
        ]
        game = TicTacToe(board)
        self.assertFalse(game.check_winner())
    
    def test_any_moves_left(self):
        board = [
            ["X", "X", "X", "X"],
            ["O", "O", "O", "O"],
            ["X", "X", "X", "X"],
            ["O", "O", "O", None]
        ]
        game = TicTacToe(board)
        self.assertFalse(game.any_moves_left())

    def test_any_moves_left_yes(self):
        board = [
            ["X", "O", "X", "X"],
            ["O", "X", "O", "O"],
            ["X", "O", "X", "X"],
            ["O", "O", "O", None]
        ]
        game = TicTacToe(board)
        self.assertTrue(game.any_moves_left())
    
    def test_no_moves_left(self):
        board = [
            ["X", "X", "X", "X"],
            ["O", "O", "O", "O"],
            ["X", "X", "X", "X"],
            ["O", "O", "O", "O"]
        ]
        game = TicTacToe(board)
        self.assertFalse(game.any_moves_left())

    def test_is_game_over_winner(self):
        board = [
            ["X", "X", "X", "X"],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None]
        ]
        game = TicTacToe(board)
        self.assertTrue(game.is_game_over())
    
    def test_is_game_over_no_moves_left(self):
        board = [
            ["X", "X", "X", "X"],
            ["O", "O", "O", "O"],
            ["X", "X", "X", "X"],
            ["O", "O", "O", "O"]
        ]
        game = TicTacToe(board)
        self.assertTrue(game.is_game_over())
    
    def test_is_game_not_over(self):
        board = [
            ["X", "X", "X", None],
            ["O", "O", "O", None],
            ["X", "X", "X", None],
            ["O", "O", "O", None]
        ]
        game = TicTacToe(board)
        self.assertFalse(game.is_game_over())


if __name__ == "__main__":
    unittest.main()