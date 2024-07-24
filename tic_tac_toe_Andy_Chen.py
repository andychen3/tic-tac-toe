# Andy Chen
# Tic-Tac-Toe Solution
from collections import defaultdict

class TicTacToe:
    def __init__(self, board):
        self.board = board
        self.winner = None
        self.players = ["O", "X"] 
 
    def check_winner(self):
        for player in self.players:
            res = self.check_board(player)
            if res != None:
                self.winner = res
                return self.winner
     
        return False

    def any_moves_left(self):
        if self.check_winner() != False:
            return False
        
        moves = 0
        for row in self.board:
            moves += row.count(None)
        
        # False means no moves left. True means move left
        return moves != 0

    def is_game_over(self):
        # if there is a winner game is over or if there is no moves but no winner
        if self.check_winner() != False or self.any_moves_left() == False:
            return True
        return False
        
    def check_board(self, player):
        diag_map = {0: 0}
        anti_diag_map = {3: 0}
        horizontal_map = {0: 0, 1: 0, 2: 0, 3: 0}
        vertical_map = {0: 0, 1: 0, 2: 0, 3: 0}
        corner_2x2_box_map = defaultdict(list)
        inner_2x2_box_map = {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}
        four_corners_set = {(0, 0), (0, 3), (3, 0), (3, 3)}
        four_corners_res = 0

        for row in range(4):
            for col in range(4):
                if self.board[row][col] == player:
                    # Check diag
                    if (row - col) in diag_map:
                        diag_map[(row - col)] += 1
                        if diag_map[(row - col)] == 4:
                            return player

                    # Check anti_diag
                    if (row + col) in anti_diag_map:
                        anti_diag_map[(row + col)] += 1
                        if anti_diag_map[(row + col)] == 4:
                            return player

                    # check horizontal
                    if row in horizontal_map:
                        horizontal_map[row] += 1
                        if horizontal_map[row] == 4:
                            return player

                    # check vertical
                    if col in vertical_map:
                        vertical_map[col] += 1
                        if vertical_map[col] == 4:
                            return player

                    # check four corners
                    if (row, col) in four_corners_set:
                        four_corners_res += 1
                        if four_corners_res == 4:
                            return player

                    # check corner 2x2 box
                    corner_2x2_box_map[(row // 2, col // 2)].append((row, col))
                    if len(corner_2x2_box_map[(row // 2, col // 2)]) == 4:
                        return player

                    # check inner 2x2 box
                    if (row, col) in inner_2x2_box_map:
                        # Check to the right, diag, and the bottom to see if matches player
                        if self.board[row][col + 1] == player \
                            and self.board[row + 1][col + 1] == player \
                                and self.board[row + 1][col] == player:
                            return player

        return None


