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

class ModifiedNode(object):
    def __init__(self, Node, distance) -> None:
        self.node = Node
        self.distance = distance


def topViewIterative(root):
    if not root:
        return
    res = list()
    map = dict()
    queue = list()
    queue.append(ModifiedNode(root, 0))
    while len(queue) > 0:
        temp = queue.pop(0)
        if temp.distance not in map:
            map[temp.distance] = temp.node.data
        if temp.node.left:
            queue.append(ModifiedNode(temp.node.left, temp.distance-1))
        if temp.node.right:
            queue.append(ModifiedNode(temp.node.right, temp.distance+1))
    for k in sorted(map):
        res.append(map[k])
    return res

def topViewRec(root, level, distance, map):
    if not root:
        return
    # res is a map; where key = distance, val = [node.val, level]
    if map.get(distance, None) is None:
        map[distance] = [root.data, level]
    else:
        if map[distance][1] > level:
             map[distance] = [root.data, level]
    topViewRec(root.left, level+1, distance-1, map)
    topViewRec(root.right, level+1, distance+1, map)

def bottomViewRec(root, level, distance, map):
    if not root:
        return
    if map.get(distance, None) is None:
        map[distance] = [root.data, level]
    else:
        if map[distance][1] < level:
            map[distance] = [root.data, level]
    bottomViewRec(root.left, level+1, distance-1, map)
    bottomViewRec(root.right, level+1, distance+1, map)

def bottomViewIterative(root):
    if not root:
        return
    res = list()
    queue = list()
    map = dict()
    queue.append(ModifiedNode(root, 0))
    while len(queue) > 0:
        temp = queue.pop(0)
        map[temp.distance] = temp.node.data
        if temp.node.left:
            queue.append(ModifiedNode(temp.node.left, temp.distance-1)) 
        if temp.node.right:
            queue.append(ModifiedNode(temp.node.right, temp.distance+1))
    for k in sorted(map):
        res.append(map[k])
    return res
    
# def bottom_view_of_tree(root):
    # if not root:
    #     return
    # Q = []
    # hd_dict = {}
    # Q.append(root)
    # while len(Q):
    #     node = Q.pop(0)
    #     hd_dict[node.horizontal_dist] = node.data

    #     if node.left:
    #         node.left.horizontal_dist = node.horizontal_dist - 1
    #         Q.append(node.left)
    #     if node.right:
    #         node.right.horizontal_dist = node.horizontal_dist + 1
    #         Q.append(node.right)
    # for k in sorted(hd_dict):
    #     print hd_dict[k],
    # print ""


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right.right = Node(25)

    print("top view iterative", end=" ")
    print(topViewIterative(root))
    print("*"*40)

    print("Top view recursive", end=" ")
    map = dict()
    topViewRec(root, 0, 0, map)
    # print(map)
    for k in sorted(map):
        print(map[k][0], end=" ")
    print()
    print("*"*40)

    print("bottom view iterative", end=" ")
    print(bottomViewIterative(root))
    print("*"*40)

    print("Bottom view of a tree recursive", end=" ")
    map = dict()
    bottomViewRec(root, 0, 0, map)
    # print(map)
    for k in sorted(map):
        print(map[k][0], end=" ")
    print()
