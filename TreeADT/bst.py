# Multiple programs for Binary Search Tree


# Node structure of Binary Search Tree
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


# search a value in a given BST
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


# search minimum value in BST. By definition leftmost value will be minimum
def search_min(cur):
    if cur is None:
        return
    else:
        if cur.left is None:
            return cur.data
        else:
            return search_min(cur.left)


# search maximum value in BST. By definition rightmost value will be maximum
def search_max(cur):
    if cur is None:
        return
    else:
        if cur.right is None:
            return cur.data
        else:
            return search_max(cur.right)


def search_max_non_recursion(cur):
    if cur is None:
        return
    while cur.right is not None:
        cur = cur.right
    return cur.data


# insert a given key in BST
def insert(root, key):
    if root is None:
        return BSTNode(key)
    else:
        if key < root.data:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


# lowest common ancestor in a BST.
# node which will have elements in left and right subtree will be lowest common ancestor
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


# check if given tree is BST or not

# for a tree to be BST, all nodes in left subtree should be less then root. Considering that; the maximum value in left
# subtree should be less then that of root value. Similarly, the minimum value in right subtree should be larger then
# the root value.
def is_bst(root):
    if root is None:
        return True
    if root.left is not None and search_max(root.left) > root.data:
        return False
    if root.right is not None and search_min(root.right) < root.data:
        return False
    if not is_bst(root.left) or not is_bst(root.right):
        return False
    return True

# idea is that the inorder traversal of a BST will produce a sorted list.
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


# kth smallest element in BST
def count_nodes(root):
    if root is None:
        return 0
    return count_nodes(root.left) + count_nodes(root.right) + 1


def kth_smallest_element(root, k):
    n = count_nodes(root.left)
    if n+1 == k:    # means root will be kth element
        return root.data
    elif n+1 < k:   # kth smallest does not lie in left subtree
        return kth_smallest_element(root.right, k-n-1)
    else:
        return kth_smallest_element(root.left, k)


# create BST from sorted array
def buildBST(A, left, right):
    if left > right:
        return
    else:
        mid = left + (right-left)//2
        newNode = BSTNode(A[mid])
        newNode.left = buildBST(A, left, mid-1)
        newNode.right = buildBST(A, mid+1, right)
    return newNode


# ceiling and floor of an input key in BST
def ceil(root, key):
    # ceiling value will always be if not on root the immediate preceding value
    val = -1
    if root is None:
        return -1
    else:
        while root is not None:
            if root.data == key:
                return root.data
            elif root.data > key:
                val = root.data
                root = root.left
            elif root.data < key:
                root = root.right
        return val


def floor(root, key):
    val = -1
    if root is None:
        return -1
    else:
        while root is not None:
            if root.data == key:
                return root.data
            elif root.data > key:
                root = root.left
            elif root.data < key:
                val = root.data
                root = root.right
        return val


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

    print "minimum value in BST:", search_min(root)
    print "maximum value in BST:", search_max(root)
    print "maximum without recursion:", search_max_non_recursion(root)

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

    k = 3
    print k, "rd smallest element is:", kth_smallest_element(root, k)

    a = [1,2,3,4,5,6,7]
    l = 0
    r = len(a)
    new_tree_root = buildBST(a, l, r-1)
    print "New BST built. Root nodes data:", new_tree_root.data

    key = 7.1
    print "ceiling value of", key, "is", ceil(root, key)
    print "floor value of", key, "is", floor(root, key)