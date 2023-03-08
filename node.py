class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.left = None
        self.right = None
        self.x_pos = x
        self.y_pos = y
    
    def get_coordinates(self):
        co_arr = (self.x_pos, self.y_pos)
        return co_arr