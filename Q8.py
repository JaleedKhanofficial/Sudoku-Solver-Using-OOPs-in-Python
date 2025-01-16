# Step 8
# The instantiation creates an empty object. The __init__ method is a special method that allows you to instantiate an object to a customized state. When a class implements an __init__ method, __init__ is automatically called upon instantiation.

# Inside your Board class, delete the spam method and replace it with an __init__ method that includes a self parameter.

class Board:
    def __init__(self):
        print('Spam!')
    
gameboard = Board()

