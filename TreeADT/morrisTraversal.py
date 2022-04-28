class Node(object):
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r


def morrisInOrder(root):
    if not root:
        return
    current = root
    while current:
        if current.l is None:
            print current.v
            current = current.r
        else:
            left = current.l
            while left.r is not None and left.r != current:
                left = left.r
            if left.r is None:
                left.r = current
                current = current.l
            else:
                left.r = None
                print current.v
                current = current.r


if __name__ == '__main__':
    if __name__ == '__main__':
        root = Node(1, Node(2, Node(4), Node(5)), Node(3))
        morrisInOrder(root)
