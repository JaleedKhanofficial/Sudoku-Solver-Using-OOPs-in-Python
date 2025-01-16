# Step 15
# The enumerate built-in function takes an iterable as its argument and returns an enumerate object you can iterate over. It provides the count (which by default starts at zero) and the value from the iterable.

# Example Code
# iterable = ['a', 'b', 'c']
# for i, j in enumerate(iterable):
    # print(i, j)
# The loop from the example above would output the tuples 0, a, 1, b, and 2, c.

# Inside the find_empty_cell method, replace pass with a for loop that uses the enumerate() function to iterate over each row in the sudoku board. Use row as the index of the current row and contents for the elements of the current row.

class Board:
    def __init__(self, board):
        self.board = board

    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
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