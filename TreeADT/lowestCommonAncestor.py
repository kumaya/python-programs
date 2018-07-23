from BinaryTree import TreeNode


def LowestCommonAncestor(root, x, y):
    if not root:
        return root
    if root.data == x or root.data == y:
        return root
    left = LowestCommonAncestor(root.left_node, x, y)
    right = LowestCommonAncestor(root.right_node, x, y)

    if left and right:
        return root
    elif not left and not right:
        return None
    elif left:
        return left
    else:
        return right


def inorder(root, io):
    if not root:
        return
    else:
        inorder(root.left_node, io)
        io.append(root.data)
        inorder(root.right_node, io)


def postorder(root, po):
    if not root:
        return
    else:
        postorder(root.left_node, po)
        postorder(root.right_node, po)
        po.append(root.data)


def lca(x, y, io, po):
    t = []
    ix = -1
    iy = -1
    for i, v in enumerate(io):
        if v == x:
            ix = i
        if v == y:
            iy = i
    if ix > iy:
        t = io[iy:ix+1]
    else:
        t = io[ix:iy+1]
    for i in po[::-1]:
        if i in t:
            return i
    return -1


if __name__ == "__main__":
    bTree = TreeNode(1)
    bTree.left_node = TreeNode(2)
    bTree.right_node = TreeNode(3)
    bTree.left_node.left_node = TreeNode(4)
    bTree.left_node.right_node = TreeNode(5)
    bTree.right_node.left_node = TreeNode(6)
    bTree.left_node.right_node.left_node = TreeNode(7)
    bTree.left_node.right_node.right_node = TreeNode(8)

    x = 4
    y = 8
    lca_node = LowestCommonAncestor(bTree, x, y)
    print "Lowest common ancestor of ", x, "and", y, "is: ", lca_node.data
    io = []
    inorder(bTree, io)
    po = []
    postorder(bTree, po)
    print "Lowest common ancestor of ", x, "and", y, "using arrays is: ", lca(x, y, io, po)