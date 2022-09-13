from collections import deque


def bfs(head):
    q = deque()

    q.append(head)

    while q:
        current = q.popleft()
        print(current.val)

        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)


def dfs(head):

    if not head:
        return

    print(head.val)

    dfs(head.left)
    dfs(head.right)


def max_depth(head):
    if not head:
        return 0

    return 1 + max(max_depth(head.left), max_depth(head.right))


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


# Binary Tree

node_1 = Node(1)
node_2, node_3, node_4, node_5 = Node(2), Node(3), Node(4), Node(5)
node_1.add_children(node_2, node_3)
node_2.add_children(node_4)
node_3.add_children(node_5, Node(6))
# node_5.add_children(Node(7))

# bfs(node_1)
# dfs(node_1)

print(max_depth(node_1))

