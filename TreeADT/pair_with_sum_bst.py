# Find a pair with given sum in a Balanced BST
from bst import BSTNode
import copy


def get_pair_with_sum(root, target):
    # Bi**h please
    s1 = copy.deepcopy([])
    # Ah! come on
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
        # if val1 +val2 is less then target; it is the fault of val1; kick it off
        # and get bigger val1
        elif val1 + val2 < target:
            flag1 = False
        # kick val2 to get smaller val2
        elif val1 + val2 > target:
            flag2 = False
        # god why did you do this.
        # pfft! time wasted
        if val1 >= val2:
            return False


def get_pair_with_sum_rec(root, node, val):
    if not node:
        return False
    orignl_root = root
    diff = val - node.data
    if has_other_pair(orignl_root, node, diff):
        first_part = val - diff
        return first_part, diff
    return get_pair_with_sum_rec(orignl_root, node.left, sum) or \
           get_pair_with_sum_rec(orignl_root, node.right, sum)


def has_other_pair(root, this_node, rem):
    if not root:
        return
    if root.data == rem and this_node!=root:
        return root.data
    elif root.data < rem:
        return has_other_pair(root.right, this_node, rem)
    elif root.data > rem:
        return has_other_pair(root.left, this_node, rem)

if __name__ == "__main__":
    root = BSTNode(4)

    root.left = BSTNode(2)
    root.right = BSTNode(6)

    root.left.left = BSTNode(1)
    root.left.right = BSTNode(3)

    root.right.left = BSTNode(5)
    root.right.right = BSTNode(7)

    sum = 4
    for sum in xrange(1, 15):
        print get_pair_with_sum(root, sum),
        print get_pair_with_sum_rec(root, root, sum)
