# Step 17
# The .index() method raises a ValueError exception when the value is not found. To prevent the program from halting execution, you'll nest this line of code inside a try block. The try statement is used to encapsulate code that might raise an exception. The except clause, on the other hand, offers alternative code to execute if an exception occurs:

# Example Code
# try:
    # <code>
# except:
    # <code>
# Put the assignment of col inside a try block. Then, create an except clause and fill its body with pass.

class Board:
    def __init__(self, board):
        self.board = board
    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:                 # step 17
                col = contents.index(0)
            except:                 # step 17
                pass                 # step 17
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