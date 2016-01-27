from BinaryTree import TreeNode


def get_leaf_node_count(root):
    if not root:
        return 0
    if not root.left_node and not root.right_node:
        return 1
    else:
        return get_leaf_node_count(root.left_node) + get_leaf_node_count(root.right_node)


# number of full nodes in a binary tree
def get_full_nodes(root, count=0):
    if not root:
        return 0
    else:
        print count
        if root.left_node and root.right_node:
            count += 1
        get_full_nodes(root.left_node, count)
        # get_full_nodes(root.right_node, count)
        return count

if __name__ == "__main__":
    bTree = TreeNode(1)

    bTree.left_node = TreeNode(2)
    bTree.right_node = TreeNode(3)

    bTree.left_node.left_node = TreeNode(4)
    bTree.left_node.right_node = TreeNode(5)

    bTree.right_node.left_node = TreeNode(6)
    bTree.right_node.right_node = TreeNode(7)

    print "Number of leaf nodes: ", get_leaf_node_count(bTree)

    print "Number of full nodes: ", get_full_nodes(bTree)
