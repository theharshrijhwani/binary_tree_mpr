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
# def get_level(n: Node):
level_gap = {1:200, 2:100, 3:50, 4:25, 5: 12, 6: 6, 7 : 3}


binary_tree = []  # all the nodes will be stored here

def preorder(n:Node, my_list:list):
    if n == None:
        return
    my_list.append(n)
    preorder(n.left, my_list)
    preorder(n.right, my_list)

def inorder(n:Node, my_list:list):
    if n == None:
        return
    inorder(n.left, my_list)
    my_list.append(n)
    inorder(n.right, my_list)

def postorder(n:Node, my_list:list):
    if n == None:
        return
    postorder(n.left, my_list)
    postorder(n.right, my_list)
    my_list.append(n)
     
def leaf_node(n:Node, leaf_list:list):
    if n == None:
        return
    
    if n.left == None and n.right == None:
        leaf_list.append(n)
        return
    
    if n.left != None:
        leaf_node(n.left, leaf_list)
    if n.right != None:    
        leaf_node(n.right, leaf_list)
      
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


def getPaths(root: Node, paths: list, path: list, allLastNode: list):
    if root is None:
        return
    path.append(root)
    if root.left is None and root.right is None:
        allLastNode.append(root)
        paths.append(path[:]) # Append a copy of the path to paths
    getPaths(root.left, paths, path, allLastNode)
    getPaths(root.right, paths, path, allLastNode)
    path.pop()

def getAllPaths(root: Node):
    paths = []
    path = []
    allLastNode = []
    getPaths(root, paths, path, allLastNode)
    paths.append(allLastNode[:])
    return paths

def search_node_list(root: Node, search_val:int, nodeList: list):
    if root == None:
        return
    if root.val == search_val:
        nodeList.append(root)
        return
    nodeList.append(root)
    if root.val < search_val:
        search_node_list(root.right, search_val, nodeList)
    else:
        search_node_list(root.left, search_val, nodeList)



def minValueNode(node: Node):
    current = node
    prev = None
    while(current.left is not None):
        prev = current
        current = current.left
    if prev:
        prev.left = None
    return current



def defcoords(parent: Node, level: int, root: Node, right: bool):
    if root == None:
        return
    if not right:
        root.x_pos = parent.x_pos - level_gap[level+1]
        root.y_pos = parent.y_pos + 100
    else:
        root.x_pos = parent.x_pos + level_gap[level+1]
        root.y_pos = parent.y_pos + 100

    root.level = parent.level + 1
    defcoords(root, level + 1, root.left, False)
    defcoords(root, level + 1, root.right, True)
    pass

def deleteNode(root: Node, key: int) -> Node:
    if not root:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
        return root
    elif key > root.val:
        root.right = deleteNode(root.right, key)
        return root
    else:
        # Case 1: Node has no child
        if not root.left and not root.right:
            return None
        # Case 2: Node has one child
        elif not root.left:
            root.right.x_pos = root.x_pos
            root.right.y_pos = root.y_pos
            root.right.level = root.level
            defcoords(root.right, root.right.level, root.right.left, False)
            defcoords(root.right, root.right.level, root.right.right, True)
            return root.right
        elif not root.right:
            root.left.x_pos = root.x_pos
            root.left.y_pos = root.y_pos
            root.left.level = root.level
            defcoords(root.left, root.left.level, root.left.left, False)
            defcoords(root.left, root.left.level, root.left.right, True)
            return root.left
        # Case 3: Node has two children
        else:
            if root.right.left == None:
                root.val = root.right.val
                root.right = root.right.right
            else:
                temp = minValueNode(root.right)
                root.val = temp.val
            return root



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

