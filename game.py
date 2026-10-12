import random

EMPTY = " "
LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
         (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
         (0, 4, 8), (2, 4, 6)]  

class Game:
    def __init__(self):
        self.board = ["", "", "", "", "", "", "", "", ""]

    def winner(self):
        """Return 'X', 'O', 'draw', or None if the game isn't over."""
        for a, b, c in LINES:
            if self.board[a] != EMPTY and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        if EMPTY not in self.board:
            return "draw"
        return None

    def available_spaces(self):
        res = []
        for space in range(len(self.board)):
            if self.board[space] == "":
                res.append(space)
        return res

    def bot_step(self, pos: int):
        self.board[pos] = "x"
        res = self.winner()
        if res == "o":
            return True, -1
        elif res == "x":
            return True, 1
        elif res == "draw":
            return True, 0
        return False, 0
