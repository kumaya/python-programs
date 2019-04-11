# Given a binary tree and a sum, determine if the tree has a root-to-leaf
# path such that adding up all the values along the path equals the given sum.

class Node(object):
    def __init__(self, d):
        self.d = d
        self.l = None
        self.r = None


def path_sum(root, sum):
    if not root:
        return False
    sum -= root.d
    if sum == 0 and not root.l and not root.r:
        return True
    return path_sum(root.l, sum) or path_sum(root.r, sum)


if __name__ == '__main__':
    root = Node(5)
    root.l = Node(4)
    root.l.l = Node(11)
    root.l.l.l = Node(17)
    root.l.l.r = Node(2)
    root.r = Node(8)
    root.r.l = Node(13)
    root.r.r = Node(4)
    root.r.r.r = Node(1)

    sum = 18
    print "root-to-leaf path with sum", sum, "exists:",
    print path_sum(root, sum)

    sum = 23
    print ""
    print "root-to-leaf path with sum", sum, "exists:",
    print path_sum(root, sum)
