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


def in_order_traversal(root):
    if not root:
        return
    else:
        in_order_traversal(root.left_node)
        print root.data,
        in_order_traversal(root.right_node)


def pre_order_traversal(root):
    if not root:
        return
    else:
        print root.data,
        pre_order_traversal(root.left_node)
        pre_order_traversal(root.right_node)


def post_order_traversal(root):
    if not root:
        return
    else:
        post_order_traversal(root.left_node)
        post_order_traversal(root.right_node)
        print root.data,


if __name__ == "__main__":
    bTree = TreeNode(1)
    bTree.left_node = TreeNode(2)
    bTree.right_node = TreeNode(3)
    bTree.left_node.left_node = TreeNode(4)
    bTree.left_node.right_node = TreeNode(5)

    print "InOrder Tree traversal:"
    in_order_traversal(bTree)

    print ""
    print "*"*80
    print "PreOrder Tree traversal"
    pre_order_traversal(bTree)

    print ""
    print "*"*80
    print "PostOrder Tree traversal"
    post_order_traversal(bTree)