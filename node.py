class Node:
    def __init__(self, _val):
        self.val = _val
        self.left = None
        self.right = None
        self.x_pos = None
        self.y_pos = None
    

FRAME_COORDINATE = [950, 655] 
root = None

binary_tree = []

def search_correct_pos(val:int, prev:Node, node: Node):
    if node == None:
        return prev
    if val < node.val:
        return search_correct_pos(val, node, node.left)
    else:
        return search_correct_pos(val, node, node.right)


def give_coordinates(n: Node):
    global root
    val = n.val
    pos = []
    if not len(binary_tree):
        root = n
        n.x_pos = FRAME_COORDINATE[0]//2
        n.y_pos = 100
    else:
        return_node = search_correct_pos(val, None, root)
        if return_node.val < val:
            return_node.right = n
            n.x_pos = return_node.x_pos + 50
            n.y_pos = return_node.y_pos + 50
        else:
            return_node.left = n
            n.x_pos = return_node.x_pos - 50
            n.y_pos = return_node.y_pos + 50
        
    binary_tree.append(n)


n1 = Node(10)
n2 = Node(50)
n3 = Node(5)
n4 = Node(100)
n5 = Node(75)


give_coordinates(n1)
give_coordinates(n2)
give_coordinates(n3)
give_coordinates(n4)
give_coordinates(n5)

for i in binary_tree:
    print(i.x_pos, i.y_pos)
