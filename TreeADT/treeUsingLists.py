# Tree implementation and basic operations


class TreeNode(object):
    """ Node structure of a tree
    """
    def __init__(self, node_val):
        self.__nodeVal = node_val
        self.__children = []

    @property
    def get_node_val(self):
        return self.__nodeVal

    @property
    def get_child(self):
        return self.__children

    def add_child(self, val):
        self.__children.append(val)


class Tree(object):
    def __init__(self):
        self.__nodes = {}

    @property
    def nodes(self):
        return self.__nodes

    def insert_node(self, node_val, parent=None):
        new_node = TreeNode(node_val)
        self[node_val] = new_node
        if parent is not None:
            self[parent].add_child(node_val)
        return new_node

    def __getitem__(self, key):
        return self.__nodes[key]

    def __setitem__(self, key, value):
        self.__nodes[key] = value

    def print_tree(self, root, depth=0):
        try:
            child = self[root].get_child
            print "\t"*depth, root
            depth += 1
            for c in child:
                self.print_tree(c, depth)
        except KeyError:
            print "No valid Entry for item '%s' found" % root

if __name__ == "__main__":
    t = Tree()
    t.insert_node("grandFather")
    t.insert_node("father", "grandFather")
    t.insert_node("uncle", "grandFather")
    t.insert_node("aunt", "grandFather")
    t.insert_node("sister", "father")
    t.insert_node("niece", "sister")
    t.insert_node("nephew", "sister")
    t.insert_node("me", "father")
    t.insert_node("cousin", "uncle")
    t.print_tree("grandFather")
    print "*"*80
    t.print_tree(4)
