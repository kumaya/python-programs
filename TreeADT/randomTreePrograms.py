from BinaryTree import TreeNode


# check existence of a path with given sum from root to any node
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

def sum_rec(t):
    if not t:
        return 0
    else:
        sum_left = sum_rec(t.left_node)
        sum_right = sum_rec(t.right_node)
        return t.data + sum_left + sum_right


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


def getNodesWithDistance(root, k):
    if not root:
        return
    if k == 0:
        print root.data
    else:
        getNodesWithDistance(root.left_node, k-1)
        getNodesWithDistance(root.right_node, k-1)


def ancestors(root, x):
    if root is None:
        return 0
    if (root.left_node == x or
            root.right_node == x or
            ancestors(root.left_node, x) or
            ancestors(root.right_node, x)):
        print root.data,
        return 1
    return 0

def getClosestNode(root, level, minDist):
    if root is None:
        return
    if root.left_node is None and root.right_node is None:
        if minDist < level:
            minDist = level
        return
    getClosestNode(root.left_node, level+1, minDist)
    getClosestNode(root.right_node, level+1, minDist)
    return minDist

if __name__ == "__main__":
    bTree = TreeNode(1)
    bTree.left_node = TreeNode(2)
    bTree.right_node = TreeNode(3)
    bTree.left_node.left_node = TreeNode(4)
    bTree.left_node.right_node = TreeNode(5)
    bTree.right_node.left_node = TreeNode(6)
    alpha = bTree.left_node.right_node.left_node = TreeNode(7)
    bTree.left_node.right_node.right_node = TreeNode(8)

    sum = 7
    print "Does tree has path: ", hasPathSum(bTree, sum)

    print "*"*80
    print "Sum of all nodes: ", add(bTree)
    print "Sum of all nodes (using recursion): ", sum_rec(bTree)

    print "*"*80
    x = 4
    y = 8
    lca_node = LowestCommonAncestor(bTree, x, y)
    print "Lowest common ancestor of ", x, "and", y, "is: ", lca_node.data

    print "*"*80
    print "Ancestors of ", alpha.data, "are: ",
    ancestors(bTree, alpha)

    print ""
    print "*"*80
    k = 2
    getNodesWithDistance(bTree, k)