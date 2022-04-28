""" Outer view of a binary tree
    20
  8   22
5   3   25
  10  14

      1
  2      3
4  5   9   11
    6    10
  7  8
"""


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leaf_nodes(r, covered_nodes):
    if not r:
        return None
    if not r.left and not r.right and r.val not in covered_nodes:
        print(r.val, end=" ")
        covered_nodes.add(r.val)
    leaf_nodes(r.left, covered_nodes)
    leaf_nodes(r.right, covered_nodes)


def left_view(r, current_level, max_level, covered_nodes):
    if not r:
        return None
    if current_level > max_level[0]:
        if r.val not in covered_nodes:
            print(r.val, end=" ")
            covered_nodes.add(r.val)
        max_level[0] = current_level
    left_view(r.left, current_level+1, max_level, covered_nodes)
    left_view(r.right, current_level+1, max_level, covered_nodes)


def right_view(r, current_level, max_level, covered_nodes):
    if not r:
        return None
    if current_level > max_level[0]:
        if r.val not in covered_nodes:
            print(r.val, end=" ")
            covered_nodes.add(r.val)
        max_level[0] = current_level
    right_view(r.right, current_level+1, max_level, covered_nodes)
    right_view(r.left, current_level+1, max_level, covered_nodes)


def outer_view(r):
    if r:
        outer_nodes = set()
        # print root node
        print(r.val, end=" ")
        outer_nodes.add(root.val)
        # print left view - already covered nodes
        left_view(r, 0, [-1], outer_nodes)
        # print leaf nodes - already covered nodes
        leaf_nodes(r, outer_nodes)
        # print right view - already covered nodes
        right_view(r, 0, [-1], outer_nodes)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.left = Node(7)
    root.left.right.right.right = Node(8)
    root.right = Node(3)
    root.right.left = Node(9)
    root.right.left.right = Node(10)
    root.right.right = Node(11)
    # root = Node(20)
    # root.left = Node(8)
    # root.right = Node(22)
    # root.left.left = Node(5)
    # root.left.right = Node(3)
    # root.left.right.left = Node(10)
    # root.left.right.right = Node(14)
    # root.right.right = Node(25)
    outer_view(root)
