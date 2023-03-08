from node import Node

TOTAL_FRAME_WIDTH = 950
TOTAL_FRAME_HEIGHT = 655

node_list = []
root = None

def get_prev_node(n: Node, val: int, pos: list):
    if n.left == None and n.right == None:
        pos.append(n.x_pos)
        pos.append(n.y_pos)
        return
    
    if n.value > val:
        get_prev_node(n.left, val)
    else:
        get_prev_node(n.right, val)
    pass

def give_coordinates_to_node(n: Node):
    if not len(node_list):
        root = n
        n.x_pos = TOTAL_FRAME_WIDTH // 2
        n.y_pos = TOTAL_FRAME_HEIGHT // 2
    else:
        pos = []
        get_prev_node(root, n.value, pos)
        n.x_pos = pos[0] + 50
        n.y_pos = pos[1] + 50
    pass
