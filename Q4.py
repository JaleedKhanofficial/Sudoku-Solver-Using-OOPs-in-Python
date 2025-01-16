# Step 4
# In order to be an instance method, a method requires a special parameter, named self by convention. This parameter is a reference to the instance of the class and must always be the first parameter.

# Add a self parameter to your spam method.

class Board:
    def spam(self):
        pass
    
gameboard = Board()