""" Left and right view of a binary tree
    20
  8   22
5   3   25
  10  14
"""

class Node(object):
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None


def leftView(root, level, maxLevel):
    if not root:
        return
    if maxLevel[0] < level:
        print root.data,
        maxLevel[0] = level
    leftView(root.left, level+1, maxLevel)
    leftView(root.right, level + 1, maxLevel)


def rightView(root, level, maxLevel):
    if not root:
        return
    if maxLevel[0] < level:
        print root.data,
        maxLevel[0] = level
    rightView(root.right, level + 1, maxLevel)
    rightView(root.left, level + 1, maxLevel)


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right.right = Node(25)

    maxLevel = [0]
    print "Left view of a tree: ",
    leftView(root, 1, maxLevel)
    print ""

    maxLevel = [0]
    print "Right view of a tree: ",
    rightView(root, 1, maxLevel)
