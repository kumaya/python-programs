from BinaryTree import TreeNode


#check existence of a path with given sum from root to any node
def hasPathSum(t1, sum):
    if not t1 or sum == 0:
        return sum == 0
    else:
        remainingSum = sum - t1.data
        if (t1.left_node and t1.right_node or
                    not t1.left_node and not t1.right_node):
            return hasPathSum(t1.left_node, remainingSum) or hasPathSum(t1.right_node, remainingSum)
        elif t1.left_node:
            return hasPathSum(t1.left_node, remainingSum)
        else:
            return hasPathSum(t1.right_node, remainingSum)


# sum of all nodes in a tree
def add(t):
    sum = 0
    Q = []
    Q.append(t)
    while len(Q) > 0:
        val = Q.pop(0)
        sum += val.data
        if val.left_node:
            Q.append(val.left_node)
        if val.right_node:
            Q.append(val.right_node)
    return sum


def LowestCommonAncestor(root, x, y):
    if not root:
        return root
    if root.data == x or root.data == y:
        return root
    left = LowestCommonAncestor(root.left_node, x, y)
    right = LowestCommonAncestor(root.right_node, x, y)

    if left and right:
        return root
    elif left:
        return left
    else:
        return right

if __name__ == "__main__":
    bTree = TreeNode(1)
    bTree.left_node = TreeNode(2)
    bTree.right_node = TreeNode(3)
    bTree.left_node.left_node = TreeNode(4)
    bTree.left_node.right_node = TreeNode(5)
    bTree.right_node.left_node = TreeNode(6)
    bTree.left_node.right_node.left_node = TreeNode(7)
    bTree.left_node.right_node.right_node = TreeNode(8)

    sum = 7
    print "Does tree has path: ", hasPathSum(bTree, sum)

    print "*"*80
    print "Sum of all nodes: ", add(bTree)

    print "*"*80
    x = 4
    y = 8
    lca_node = LowestCommonAncestor(bTree, x, y)
    print "Lowest common ancestor of ", x, "and", y, "is: ", lca_node.data

