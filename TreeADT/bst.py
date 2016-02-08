# Multiple programs for Binary Search Tree


class BSTNode(object):
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None

    @property
    def data(self):
        return self.__data

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, l):
        self.__left = l

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, r):
        self.__right = r


def search(cur, key):
    if cur is None:
        return None
    while cur:
        if key == cur.data:
            return "Found"
        elif key < cur.data:
            cur = cur.left
        else:
            cur = cur.right
    return "Not Found"


def searchMin(cur):
    if cur is None:
        return
    else:
        if cur.left is None:
            return cur.data
        else:
            return searchMin(cur.left)


def searchMax(cur):
    if cur is None:
        return
    else:
        if cur.right is None:
            return cur.data
        else:
            return searchMax(cur.right)


def insert(root, key):
    if root is None:
        return BSTNode(key)
    else:
        if key < root.data:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def lowest_common_ancestor(root, x, y):
    if root is None:
        return root
    while True:
        if (y >= root.data >= x) or (x >= root.data >= y):
            return root.data
        elif root.data > x:
            root = root.left
        else:
            root = root.right

if __name__ == "__main__":
    root = BSTNode(4)

    root.left = BSTNode(2)
    root.right = BSTNode(6)

    root.left.left = BSTNode(1)
    root.left.right = BSTNode(3)

    root.right.left = BSTNode(5)
    root.right.right = BSTNode(7)

    val = 15
    print "Search", val, "in BST: ", search(root, 15)

    print "minimum value in BST: ", searchMin(root)
    print "maximum value in BST: ", searchMax(root)

    x = 1
    y = 12
    print "LCA of", x, "and", y, "is", lowest_common_ancestor(root, x, y)