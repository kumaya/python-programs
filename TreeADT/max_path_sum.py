# Given a binary tree, find the maximum path sum. The path may start and
# end at any node in the tree.

class Node(object):
    def __init__(self, d):
        self.d = d
        self.l = None
        self.r = None


def max_path_sum(root, maxi):
    if not root:
        return 0
    left = max_path_sum(root.l, maxi)
    right = max_path_sum(root.r, maxi)
    max_lr = max(left, right)
    max_single = max(max_lr+root.d, root.d)
    max_all = max(max_single, root.d+left+right)
    maxi[0] = max(maxi[0], max_all)
    return max_single


if __name__ == '__main__':
    root = Node(10)
    root.l = Node(2)
    root.l.l = Node(20)
    root.l.r = Node(1)
    root.r = Node(10)
    root.r.r = Node(-25)
    root.r.r.l = Node(3)
    root.r.r.r = Node(4)

    maxi = [-1000000]
    max_path_sum(root, maxi)
    print "Max path sum: ", maxi[0]
