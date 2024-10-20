class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            self.left = self.check_and_instance_node(self.left, value)
        else:
            self.right = self.check_and_instance_node(self.right, value)
    
    def find(self, value):
        if value < self.value:
            if not self.left:
                raise "NotFound"
            return self.left.find(value)
        if not self.right:
            raise "NotFound"
        return self.right.find(value)


    @classmethod
    def check_and_instance_node(cls, side, value):
        if not side:
            return Tree(value)
        return side.insert(value)

tree_node = Tree(15)
tree_node.insert(10)
tree_node.insert(100)
tree_node.insert(20)
tree_node.insert(1)
tree_node.insert(3)
tree_node.insert(20)
print(tree_node.value)