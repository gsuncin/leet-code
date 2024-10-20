class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def get_inorder(root, nodes= []):
    if not root:
        return
    get_inorder(root.left, nodes)
    nodes.append(root.info)
    get_inorder(root.right, nodes)
    return nodes

def pre_order(root, nodes= []):
    if not root:
        return
    nodes.append(root.info)
    pre_order(root.left, nodes)
    pre_order(root.right, nodes)
    return nodes

def post_order(root, nodes= []):
    if not root:
        return
    post_order(root.left, nodes)
    post_order(root.right, nodes)
    nodes.append(root.info)
    return nodes

def levelOrder(root):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop()
        if node:
            print(node.info, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

tree = BinarySearchTree()
t = 6
arr = [1, 2, 5, 3, 6, 4]

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)