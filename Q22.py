# Step 22
# find_empty_cell is returning (0, 0), which is the position of the first empty cell in the sudoku board.

# Turn the first 0 inside puzzle into a 1. You will see in the output that the next empty cell will be found.

class Board:
    def __init__(self, board):
        self.board = board

    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None
puzzle = [
  [1, 0, 2, 0, 0, 8, 0, 0, 0],              # step 22
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
print(gameboard.find_empty_cell())