
class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def get_val(self):
        return self.val

    def add_children(self, left=None, right=None):
        self.left = left
        self.right = right


def check_equal_tree(tree_1, tree_2):

    if tree_1 is None and tree_2 is None:
        return True

    if tree_1 is None or tree_2 is None:
        return False

    if tree_1.get_val() == tree_2.get_val():
        return check_equal_tree(tree_1.left, tree_2.left) and check_equal_tree(tree_1.right, tree_2.right)

    return False


node_1 = Node(1)
node_2, node_3, node_4, node_5 = Node(2), Node(3), Node(4), Node(5)

node_1.add_children(node_2, node_3)
node_2.add_children(node_4)
node_3.add_children(node_5)

node_a = Node(1)


node_a.add_children(node_2, node_3)

x = check_equal_tree(node_1, node_a)
print(x)