# Program to find maximum element in a tree

from BinaryTree import TreeNode


def maximum_node(root):
    # if not root:
    #     return
    # return max(maximum_node(root.left_node), maximum_node(root.right_node), root.data)
    max = 0
    if root:
        root_data = root.data
        left = maximum_node(root.left_node)
        right = maximum_node(root.right_node)

        if left > right:
            max = left
        else:
            max = right
        if root_data > max:
            max = root_data
    return max


if __name__ == "__main__":
    bTree = TreeNode(1)
    bTree.left_node = TreeNode(2)
    bTree.right_node = TreeNode(3)
    bTree.left_node.left_node = TreeNode(4)
    bTree.left_node.right_node = TreeNode(5)

    print "Maximum node value: ",
    print maximum_node(bTree)
