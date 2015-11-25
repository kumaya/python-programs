# Binary tree implementation


class TreeNode(object):
    def __init__(self, value=None):
        self.__data = value
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


class BinaryTree(object):
    def __add_node(self, data):
        return TreeNode(data)

    def insert(self, root, data):
        if not root:
            return self.__add_node(data)
        else:
            if root.data <= data:
                root.left_node = self.insert(root.left_node, data)
            else:
                root.right_node = self.insert(root.right_node, data)
        return root

    def search(self, root, value):
        try:
            if not root:
                raise AttributeError
            else:
                if value == root.data:
                    print "Found"
                else:
                    if root.data <= value:
                        self.search(root.left_node, value)
                    else:
                        self.search(root.right_node, value)
        except (KeyError, AttributeError):
            print "Not found."

    def depth(self, root_node):
        if not root_node:
            return 0
        else:
            ldepth = self.depth(root_node.left_node)
            rdepth = self.depth(root_node.right_node)
            return max(ldepth, rdepth) + 1

    def delete(self, root, value):
        pass

    @staticmethod
    def print_tree(root_node, depth=0):
        try:
            if not root_node:
                return 0
            else:
                depth += 1
                BinaryTree.print_tree(root_node.left_node, depth)
                print root_node.data,
                BinaryTree.print_tree(root_node.right_node, depth)
        except (KeyError, AttributeError):
            print "Root value not found"


if __name__ == "__main__":
    bTree = BinaryTree()
    root = bTree.insert(root=None, data=1)
    bTree.insert(root, 2)
    bTree.insert(root, 3)
    bTree.insert(root, 4)
    bTree.insert(root, 5)
    print "Printing Binary tree: "
    BinaryTree.print_tree(root)

    print ""
    print "*"*80
    val = 510
    print "Searching value %d in the tree:" % val,
    bTree.search(root, val)
    val = 41
    print "Searching value %d in the tree:" % val,
    bTree.search(root, val)

    print "*"*80
    print "Maximum depth of tree: ", bTree.depth(root)
