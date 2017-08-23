"""
@Problem Statement:
One of the many ways of representing a tree is to have an array(of length same
as number of nodes), where each element in the node denotes the parent of that
node.
{-1, 0, 0, 1, 1} would represent a tree with -
    * 0 as root
    * 1 and 2 as children of 0
    * 3 and 4 as children of 1
Given a similar representation, print reverse level order traversal of the
corresponding tree.
Level order traversal of a tree is where we traverse levels of tree one by one.
@Input:
N: Length of tree
treeNode: representation of tree
"""


def reverse_parent_tree(root, tree):
    # base case for recursive call
    if not root:
        return

    nodes = root
    root = []
    for node in nodes:
        if node in tree:
            root += tree[node]
    reverse_parent_tree(root, tree)
    print " ".join(nodes)


def rev_par_tree(lst, mapping):
    if not lst:
        return
    q = []
    s = []
    q.append(lst)
    while q:
        childrens = q.pop(0)
        for child in reversed(childrens):
            s.append(child)
            q.append(mapping[child])
    while s:
        print s.pop(),


# N = 5
# treeNode = ['-1', '0', '0', '2', '1']
N = 9
treeNode = ['8', '7', '0', '5', '5', '8', '7', '0', '-1']

print "*****METHOD 1*****"
parent = {}
for index,val in enumerate(treeNode):
    if val in parent:
        parent[val].append(str(index))
    else:
        parent[val] = [str(index)]

print parent
reverse_parent_tree(parent['-1'], parent)

print "*****METHOD 2*****"
treeNode = [8, 7, 0, 5, 5, 8, 7, 0, -1]
from collections import defaultdict
parent = defaultdict(list)
for index, val in enumerate(treeNode):
    parent[val].append(index)

print parent
rev_par_tree(parent[-1], parent)