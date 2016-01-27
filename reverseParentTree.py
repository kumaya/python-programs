"""
@Problem Statement:
One of the many ways of representing a tree is to have an array(of length same as number of nodes), 
where each element in the node denotes the parent of that node.
{-1, 0, 0, 1, 1} would represent a tree with -
    * 0 as root
    * 1 and 2 as children of 0
    * 3 and 4 as children of 1
Given a similar representation, print reverse level order traversal of the corresponding tree.
Level order traversal of a tree is where we traverse levels of tree one by one.
@Input:
N: Length of tree
treeNode: representation of tree
"""


def reverse_parent_tree(tree, root):
    # base case for recursive call
    if len(tree) == 0:
        return

    ret = tree
    tree = []
    for node in ret:
        if node in root:
            tree += root[node]
    reverse_parent_tree(tree, root)
    print " ".join(ret)


# N = 5
# treeNode = ['-1', '0', '0', '2', '1']
N = 9
treeNode = ['8', '7', '0', '5', '5', '8', '7', '0', '-1']
parent = {}

for index,val in enumerate(treeNode):
    if val in parent:
        parent[val].append(str(index))
    else:
        parent[val] = [str(index)]

# print parent

reverse_parent_tree(parent['-1'], parent)