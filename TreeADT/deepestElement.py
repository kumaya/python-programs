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

if __name__ == "__main__":
    bTree = TreeNode(1)
    bTree.left_node = TreeNode(2)
    bTree.right_node = TreeNode(3)
    bTree.left_node.left_node = TreeNode(4)
    bTree.left_node.right_node = TreeNode(5)
    bTree.left_node.left_node.left_node = TreeNode(12)

    print "Deepest element is: ", deepest_element(bTree)
