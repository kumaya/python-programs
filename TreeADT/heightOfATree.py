# Find the height of a tree
from BinaryTree import TreeNode


# height using recursion
def height_using_recursion(root):
    if not root:
        return 0
    else:
        left = height_using_recursion(root.left_node)
        right = height_using_recursion(root.right_node)
        return max(left, right) + 1


# height without using recursion
def height_without_recursion(root):
    Q = []
    height = 0
    Q.append(root)

    # marker to calculate height. After every level into queue, an empty value
    # will get inserted. Reading this empty value, we can thus calculate height.
    Q.append("NULL")
    while len(Q) > 0:
        root = Q.pop(0)
        if root == "NULL":
            if len(Q) > 0:
                Q.append("NULL")
            height += 1
        else:
            if root.left_node:
                Q.append(root.left_node)
            if root.right_node:
                Q.append(root.right_node)
    return height

if __name__ == "__main__":
    bTree = TreeNode(1)
    bTree.left_node = TreeNode(2)
    bTree.right_node = TreeNode(3)
    bTree.left_node.left_node = TreeNode(4)
    bTree.left_node.right_node = TreeNode(5)
    bTree.left_node.left_node.left_node = TreeNode(12)

    print "Height using recursion: ", height_using_recursion(bTree)

    print "Height without using recursion: ", height_without_recursion(bTree)