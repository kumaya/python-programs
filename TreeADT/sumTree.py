# A sumTree is a binary tree where the value of a node is equal to sum of the
# nodes present in its left subtree and right subtree. An empty tree is a
# sumTree. A leaf node is a sum tree.

class Node(object):
    def __init__(self, data):
        self.val = data
        self.l = None
        self.r = None

def isLeaf(root):
    if not root:
        return False
    if not root.l and not root.r:
        return True
    return False

def sum(root):
    if not root:
        return 0
    return sum(root.l) + root.val + sum(root.r)

# O(n^2)
def isSumTreeO2(root):
    # an empty tree is sum tree
    if not root:
        return True
    # leaf node is a sum tree
    if isLeaf(root):
        return True
    lSum = sum(root.l)
    rSum = sum(root.r)
    # if node is sum tree and its children are sum trees
    if (lSum + rSum == root.val) and isSumTreeO2(root.l) and isSumTreeO2(root.r):
        return True
    return False

# O(n)
def isSumTreeOn(root):
    # an empty tree is a sum tree
    if not root:
        return True
    # leaf node is sum tree
    if isLeaf(root):
        return True
    if isSumTreeOn(root.l) and isSumTreeOn(root.r):
        # check left children
        if not root.l:
            lSum = 0
        elif isLeaf(root.l):
            lSum = root.l.val
        else:
            lSum = 2 * root.l.val

        # check right child
        if not root.r:
            rSum = 0
        elif isLeaf(root.r):
            rSum = root.r.val
        else:
            rSum = 2 * root.r.val

        if lSum + rSum == root.val:
            return True
    return False


if __name__ == '__main__':
    root = Node(26)
    root.l = Node(10)
    root.l.l = Node(4)
    root.l.r = Node(6)
    root.r = Node(3)
    root.r.r = Node(3)
    # root = Node(20)
    # root.l = Node(10)
    # root.l.r = Node(5)
    # root.l.r.l = Node(5)

    print isSumTreeO2(root)
    print isSumTreeOn(root)
    print sum(root)
