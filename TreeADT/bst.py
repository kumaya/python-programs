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


def searchMax2(cur):
    if cur is None:
        return
    while cur.right is not None:
        cur = cur.right
    return cur.data


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


def is_bst(root):
    if root is None:
        return True
    if root.left is not None and searchMax(root.left) > root.data:
        return False
    if root.right is not None and searchMin(root.right) < root.data:
        return False
    if not is_bst(root.left) or not is_bst(root.right):
        return False
    return True


def is_bst_inorder(root, prev=[]):
    if root is None:
        return
    else:
        is_bst_inorder(root.left, prev)
        prev.append(root.data)
        is_bst_inorder(root.right, prev)
    return prev

def check(val):
    for i in xrange(len(val)-1):
        if val[i] > val[i+1]:
            return False
    return True


# Inorder successor and predecessor of BST
def get_pre_suc(root, key, pre, suc):
    if root is None:
        return
    if root.data == key:
        if root.left is not None:
            temp = root.left
            while temp.right is not None:
                temp = temp.right
            pre = temp

        if root.right is not None:
            temp = root.right
            while temp.left is not None:
                temp = temp.left
            suc = temp
        return pre.data, suc.data
    if root.data > key:
        suc = root
        return get_pre_suc(root.left, key, pre, suc)
    else:
        pre = root
        return get_pre_suc(root.right, key, pre, suc)


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

    print "minimum value in BST:", searchMin(root)
    print "maximum value in BST:", searchMax(root)
    print "maximum without recursion:", searchMax2(root)

    x = 1
    y = 12
    print "LCA of", x, "and", y, "is", lowest_common_ancestor(root, x, y)

    print "Tree is BST:", is_bst(root)
    print "Tree is BST using in order traversal", check(is_bst_inorder(root))

    key = 6
    suc = None
    pre = None
    val = get_pre_suc(root, key, suc, pre)
    print "predecessor and successor of", key, "are", val[0], val[1]