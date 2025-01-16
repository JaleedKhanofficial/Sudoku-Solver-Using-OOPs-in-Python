# Step 6
# To call an instance method, you need to use dot notation:

# Example Code
# instance_name.method_name()
# Where instance_name is the instance or object, and method_name is the method you want to call.

# Call the spam method of the gameboard object.

class Board:
    def spam(self):
        print('Spam!')
    
gameboard = Board()
gameboard.spam()