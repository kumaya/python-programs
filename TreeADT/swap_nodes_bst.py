# Swap nodes in an incorrect BST to correct it
from bst import BSTNode


def swap(a, b):
    a.data = b.data
    b.data = a.data
    a.data = b.data


def swap_nodes_bst(root, first, middle, last, prev):
    if root is not None:
        swap_nodes_bst(root.left, first, middle, last, prev)
        if prev and root.data < prev.data:
            if not first:
                first = prev
                middle = root
            else:
                last = root
        prev = root
        swap_nodes_bst(root.right, first, middle, last, prev)



if __name__ == "__main__":
    root = BSTNode(4)

    root.left = BSTNode(2)
    root.right = BSTNode(6)

    root.left.left = BSTNode(1)
    root.left.right = BSTNode(3)

    root.right.left = BSTNode(5)
    root.right.right = BSTNode(7)
