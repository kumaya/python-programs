# Program to detect isomorphic trees
# Two trees are isomorphic iff:
#   data of t1 and t2 are same
#   left child of t1 is isomorphic to left child of t2 and right child of t1 to right child of t2 or
#   left child of t1 is isomorphic to right chilf of t2 and vice-versa
from BinaryTree import TreeNode


def is_isomorphic(t1, t2):
    # Base case: If both trees are empty, they are isomorphic by definition
    if not t1 and not t2:
        return True
    # If one of them is non empty, violates isomorphism
    if not t1 or not t2:
        return False
    # If data in a level are not same; violates isomorphism
    if t1.data != t2.data:
        return False
    else:
        case1 = (is_isomorphic(t1.left_node, t2.left_node) and
                 is_isomorphic(t1.right_node, t2.right_node))
        case2 = (is_isomorphic(t1.left_node, t2.right_node) and
                 is_isomorphic(t1.right_node, t2.left_node))
        return case1 or case2

if __name__ == "__main__":
    bTree1 = TreeNode(1)
    bTree1.left_node = TreeNode(2)
    bTree1.right_node = TreeNode(3)
    bTree1.left_node.left_node = TreeNode(4)
    bTree1.left_node.right_node = TreeNode(5)
    bTree1.right_node.left_node = TreeNode(6)
    bTree1.left_node.right_node.left_node = TreeNode(7)
    bTree1.left_node.right_node.right_node = TreeNode(8)

    bTree2 = TreeNode(1)
    bTree2.left_node = TreeNode(3)
    bTree2.right_node = TreeNode(2)
    bTree2.left_node.right_node = TreeNode(6)
    bTree2.right_node.left_node = TreeNode(4)
    bTree2.right_node.right_node = TreeNode(5)
    bTree2.right_node.right_node.left_node = TreeNode(8)
    bTree2.right_node.right_node.right_node = TreeNode(7)

    print is_isomorphic(bTree1, bTree2)



