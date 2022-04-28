"""
Given a binary tree print the top view and bottom view
    20
  8   22
5   3   25
  10  14
"""


class Node(object):
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.horizontal_dist = 0


def top_view_of_tree(root):
    if not root:
        return
    Q = []
    hd_dict = {}
    Q.append(root)
    while len(Q):
        node = Q.pop(0)
        if node.horizontal_dist not in hd_dict:
            hd_dict[node.horizontal_dist] = node.data
        if node.left:
            node.left.horizontal_dist = node.horizontal_dist - 1
            Q.append(node.left)
        if node.right:
            node.right.horizontal_dist = node.horizontal_dist + 1
            Q.append(node.right)
    for k in sorted(hd_dict):
        print hd_dict[k],
    print ""


def topViewRecursion(root, height, hd, globalMap):
    if not root:
        return
    if globalMap.get(hd, None) is None:
        globalMap[hd] = [root.data, height]
    else:
        if globalMap[hd][1] > height:
            globalMap[hd] = [root.data, height]
    topViewRecursion(root.left, height+1, hd-1, globalMap)
    topViewRecursion(root.right, height+1, hd+1, globalMap)


def bottom_view_of_tree(root):
    if not root:
        return
    Q = []
    hd_dict = {}
    Q.append(root)
    while len(Q):
        node = Q.pop(0)
        hd_dict[node.horizontal_dist] = node.data

        if node.left:
            node.left.horizontal_dist = node.horizontal_dist - 1
            Q.append(node.left)
        if node.right:
            node.right.horizontal_dist = node.horizontal_dist + 1
            Q.append(node.right)
    for k in sorted(hd_dict):
        print hd_dict[k],
    print ""


def bottomViewRecursion(root, height, hd, globalMap):
    if not root:
        return
    if globalMap.get(hd, None) is None:
        globalMap[hd] = [root.data, height]
    else:
        if globalMap[hd][1] < height:
            globalMap[hd] = [root.data, height]
    bottomViewRecursion(root.left, height+1, hd-1, globalMap)
    bottomViewRecursion(root.right, height+1, hd+1, globalMap)


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right.right = Node(25)

    print "Top view of a tree"
    top_view_of_tree(root)

    print "Top view of a tree recursion"
    map = dict()
    topViewRecursion(root, 0, 0, map)
    print map
    for i in sorted(map.items()):
        print i[1][0],
    print ""

    print "Bottom view of a tree"
    bottom_view_of_tree(root)
    print "Bottom view of a tree recursion"
    map = dict()
    bottomViewRecursion(root, 0, 0, map)
    for i in sorted(map.items()):
        print i[1][0],
    print ""
