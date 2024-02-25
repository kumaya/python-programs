# InOrder, Preorder and Postorder traversal.


class TreeNode(object):
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None

    @property
    def data(self):
        return self.__data

    @property
    def left_node(self):
        return self.__left

    @left_node.setter
    def left_node(self, left):
        self.__left = left

    @property
    def right_node(self):
        return self.__right

    @right_node.setter
    def right_node(self, right):
        self.__right = right


def in_order_traversal_recursion(root):
    if not root:
        return
    else:
        in_order_traversal_recursion(root.left_node)
        print(root.data, end=" ")
        in_order_traversal_recursion(root.right_node)

# left, root, right
def inOrder(root):
    res = list()
    stack = list()
    while len(stack) > 0 or root is not None:
        while root is not None:
            stack.append(root)
            root = root.left_node
        root = stack.pop()
        res.append(root.data)
        root = root.right_node
    return res

def pre_order_traversal_recursion(root):
    if not root:
        return
    else:
        print(root.data, end= " ")
        pre_order_traversal_recursion(root.left_node)
        pre_order_traversal_recursion(root.right_node)

# root, left, right
def preOrder(root):
    res = list()
    stack = list()
    stack.append(root)
    while len(stack) > 0:
        root = stack.pop()
        res.append(root.data)
        if root.right_node:
            stack.append(root.right_node)
        if root.left_node:
            stack.append(root.left_node)
    return res


def post_order_traversal_recursion(root):
    if not root:
        return
    else:
        post_order_traversal_recursion(root.left_node)
        post_order_traversal_recursion(root.right_node)
        print(root.data, end=" ")

# left, right, root
def postOrder(root):
    res = list()
    stack = list()
    while len(stack) > 0 or root is not None:
        if root is not None:
            stack.append(root)
            root = root.left_node
        else:
            temp = stack[-1].right_node
            if temp is not None:
                root = temp
            else:
                temp = stack.pop()
                res.append(temp.data)
                while len(stack) > 0 and stack[-1].right_node == temp:
                    temp = stack.pop()
                    res.append(temp.data)
    return res

def levelOrderTraversal(root):
    Q = []
    Q.append(root)
    while len(Q) > 0:
        root = Q.pop(0)
        print(root.data, end= " ")
        if root.left_node:
            Q.append(root.left_node)
        if root.right_node:
            Q.append(root.right_node)

def levelBylevel_OrderTraversal(root):
    res = list()
    Q = []
    Q.append(root)
    while len(Q) > 0:
        # res.append([t.data for t in Q])
        q = list()
        x = list()
        while len(Q) > 0:
            temp = Q.pop(0)
            x.append(temp.data)
            if temp.left_node is not None:
                q.append(temp.left_node)
            if temp.right_node is not None:
                q.append(temp.right_node)
        Q = q
        res.append(x)
    return res

def height(root):
    if not root:
        return 0
    else:
        return max(height(root.left_node), height(root.right_node)) + 1

def printSpiralRecursion(node, level, flag):
    if not node:
        return
    if level == 0:
        print(node.data, end=" ")
    elif level > 0:
        if flag:
            printSpiralRecursion(node.left_node, level - 1, flag)
            printSpiralRecursion(node.right_node, level - 1, flag)
        else:
            printSpiralRecursion(node.right_node, level - 1, flag)
            printSpiralRecursion(node.left_node, level - 1, flag)

def spiralIterative(root):
    res = list()
    stack = list()
    flag = False
    stack.append(root)
    while len(stack) > 0:
        for i in stack:
            res.append(i.data)
        q = list()
        while len(stack) > 0:
            t = stack.pop()
            if flag:
                if t.left_node:
                    q.append(t.left_node)
                if t.right_node:
                    q.append(t.right_node)
            else:
                if t.right_node:
                    q.append(t.right_node)
                if t.left_node:
                    q.append(t.left_node)
        stack = q
        flag = not flag
    return res


if __name__ == "__main__":
    bTree = TreeNode(1)
    bTree.left_node = TreeNode(2)
    bTree.right_node = TreeNode(3)
    bTree.left_node.left_node = TreeNode(4)
    bTree.left_node.right_node = TreeNode(5)

    print("InOrder Tree traversal:", end=" ")
    in_order_traversal_recursion(bTree)
    print()
    print("InOrder iterative:", inOrder(bTree))

    print("*"*80)
    print("PreOrder Tree traversal", end=" ")
    pre_order_traversal_recursion(bTree)
    print()
    print("PreOrder iterative:", preOrder(bTree))

    print("*"*80)
    print("PostOrder Tree traversal", end=" ")
    post_order_traversal_recursion(bTree)
    print()
    print("PostOrder iterative:", postOrder(bTree))

    print("*"*80)
    print("LevelOrder Tree traversal", end=" ")
    levelOrderTraversal(bTree)
    print()
    
    res = levelBylevel_OrderTraversal(bTree)
    print("Level By Level Order Tree traversal", res, end=" ")

    print()
    print("*"*80)
    print("spiral recursion: ", end=" ")
    flag = True
    for level in range(height(bTree)):
        printSpiralRecursion(bTree, level, flag)
        flag = not flag
    print()
    print("Spiral iterative: ", spiralIterative(bTree))