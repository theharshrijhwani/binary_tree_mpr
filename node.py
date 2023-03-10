class Node:
    def __init__(self, _val):
        self.val = _val
        self.left = None
        self.right = None
        self.x_pos = None
        self.y_pos = None
        self.level = None
    

FRAME_COORDINATE = [950, 655] 
root = None 

binary_tree = []  # all the nodes will be stored here

def search_correct_pos(val:int, prev:Node, node: Node):
    if node == None:
        return prev
    if val < node.val:
        return search_correct_pos(val, node, node.left)
    else:
        return search_correct_pos(val, node, node.right)

def search_node(val):
    for i in binary_tree:
        if i.val == val:
            return i;
    return None;

# def get_level(n: Node):
level_gap = {1:200, 2:100, 3:50, 4:25}


prev_coordinates = []
def give_coordinates(n: Node):
    global root # using root which is global
    n.level = 0
    val = n.val
    # pos = []
    if not len(binary_tree):
        root = n
        n.x_pos = FRAME_COORDINATE[0]//2
        n.y_pos = 100
        
    else:
        while len(prev_coordinates):
            prev_coordinates.pop()
        # this will store coordinates of previous node
        return_node = search_correct_pos(val, None, root) # the return_node is first assigned with root node and then it gradually traverses
        n.level = return_node.level+1
        if return_node.val < val:
            return_node.right = n
            n.x_pos = return_node.x_pos + level_gap[n.level]
            n.y_pos = return_node.y_pos + 100
        else:
            return_node.left = n
            n.x_pos = return_node.x_pos - level_gap[n.level]
            n.y_pos = return_node.y_pos + 100
        prev_coordinates.append(return_node.x_pos)
        prev_coordinates.append(return_node.y_pos)
        prev_coordinates.append(return_node.val)
    binary_tree.append(n)
    return prev_coordinates

