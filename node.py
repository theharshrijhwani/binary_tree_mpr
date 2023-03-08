from operations import *

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.x_pos = None
        self.y_pos = None
        give_coordinates_to_node(self)

    
    def get_coordinates(self):
        co_arr = (self.x_pos, self.y_pos)
        return co_arr
    

n = Node(10)
print(n.get_coordinates())