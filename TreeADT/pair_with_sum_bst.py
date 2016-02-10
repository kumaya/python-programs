# Find a pair with given sum in a Balanced BST
from bst import BSTNode
import copy


def get_pair_with_sum(root, target):
    s1 = copy.deepcopy([])
    s2 = copy.deepcopy([])
    cur1 = root
    cur2 = root
    flag1 = flag2 = False
    val1 = val2 = 0
    while True:
        # in-order traversal
        while not flag1:
            if cur1 is not None:
                s1.append(cur1)
                cur1 = cur1.left
            else:
                if len(s1) <= 0:
                    flag1 = True
                else:
                    cur1 = s1.pop()
                    val1 = cur1.data
                    cur1 = cur1.right
                    flag1 = True
        # reverse in-order traversal
        while not flag2:
            if cur2 is not None:
                s2.append(cur2)
                cur2 = cur2.right
            else:
                if len(s2) <= 0:
                    flag2 = True
                else:
                    cur2 = s2.pop()
                    val2 = cur2.data
                    cur2 = cur2.left
                    flag2 = True
        if val1 != val2 and val1 + val2 == target:
            return val1, val2
        elif val1 + val2 < target:
            flag1 = False
        elif val1 + val2 > target:
            flag2 = False
        if val1 >= val2:
            return False



if __name__ == "__main__":
    root = BSTNode(4)

    root.left = BSTNode(2)
    root.right = BSTNode(6)

    root.left.left = BSTNode(1)
    root.left.right = BSTNode(3)

    root.right.left = BSTNode(5)
    root.right.right = BSTNode(7)

    sum = 8
    print get_pair_with_sum(root, sum)