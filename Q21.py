# Step 21
# Test that the find_empty_cell method works properly by calling it on gameboard and printing the result.

# Note that, although find_empty_cell is defined with one parameter, you must not give it a value by passing an argument to the function call, since self is automatically passed in as the object you are calling the method on.

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
print(gameboard.find_empty_cell())              # step 21