# Step 19
# If the code inside the try block raises an exception, you want the program to continue running, and the pass statement accomplishes this.

# Although this code works, specifying the exception type after the except keyword is considered good practice.

# Since you know that a ValueError might be raised, leave a space after the except keyword and add ValueError after that.

class Board:
    def __init__(self, board):
        self.board = board
    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:          # step 19
                pass
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

gameboard = Board(puzzle)