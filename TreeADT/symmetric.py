class Node(object):
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None


def isSymmetric(root1, root2):
    # if both the tree are empty they are symmetrical
    if not root1 and not root2:
        return True
    if root1 and root2:
        # if root data is same in that case, left subtree of tree1 should be
        # equal to right subtree of tree2 and vice versa.
        if root1.data == root2.data:
            return isSymmetric(root1.left, root2.right) and\
                   isSymmetric(root1.right, root2.left)
    return False


def isMirror(root):
    return isSymmetric(root, root)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.right.right = Node(3)
    print "Is Mirror: ", isMirror(root)

    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    root2 = Node(1)
    root2.left = Node(3)
    root2.right = Node(2)
    root2.right.left = Node(5)
    root2.right.right = Node(4)

    print "Is symmetric: ", isSymmetric(root1, root2)
