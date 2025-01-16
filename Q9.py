# Step 9
# The sudoku puzzle to solve will be a list of lists, as the following:

# Example Code
# [
#   [0, 0, 2, 0, 0, 8, 0, 0, 0],
#   [0, 0, 0, 0, 0, 3, 7, 6, 2],
#   [4, 3, 0, 0, 0, 0, 8, 0, 0],
#   [0, 5, 0, 0, 3, 0, 0, 9, 0],
#   [0, 4, 0, 0, 0, 0, 0, 2, 6],
#   [0, 0, 0, 4, 6, 7, 0, 0, 0],
#   [0, 8, 6, 7, 0, 4, 0, 0, 0],
#   [0, 0, 0, 5, 1, 9, 0, 0, 8],
#   [1, 7, 0, 0, 0, 6, 0, 0, 5]
# ]
# Note that the empty cells are filled with a zero.

# Declare a puzzle variable and assign it the list of lists in the example above.

class Board:
    def __init__(self):
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
gameboard = Board()