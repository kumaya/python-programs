from BinaryTree import TreeNode


def deepest_element(root):
    Q = []
    Q.append(root)
    while len(Q) > 0:
        temp = Q.pop(0)
        if temp.left_node:
            Q.append(temp.left_node)
        if temp.right_node:
            Q.append(temp.right_node)
    return temp.data


def deepest_element_recr(root, level, t):
    if not root:
        return
    else:
        if t[0] < level:
            t[0] = level
            t[1] = root.data
        left = deepest_element_recr(root.left_node, level+1, t)
        right = deepest_element_recr(root.right_node, level+1, t)

if __name__ == "__main__":
    bTree = TreeNode(1)
    bTree.left_node = TreeNode(2)
    bTree.right_node = TreeNode(3)
    bTree.right_node.left_node = TreeNode(4)
    bTree.right_node.right_node = TreeNode(5)
    bTree.right_node.left_node.right_node = TreeNode(12)

    print "Deepest element is: ", deepest_element(bTree)

    # using recursion
    level = 0
    t = [-1, -1]    # max_level and result
    deepest_element_recr(bTree, level, t)
    print "Deepest element (using recursion) is: ", t[1]
