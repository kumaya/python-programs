"""
BACKTRACKING TEMPLATE
def solve(c->all choices):
    if is_solved(...):
        return True/False or print
    for c in all choices:
        if is_valid(c):
            update choice c
            if solve(c):
                return True/False
            revert choice c
"""

# Write a program to print all permutations of a given string


def printString(l):
    s = "".join(l)
    return s


def permute(arr, l, r):
    if l == r:
        print(printString(arr), end=" ")
    else:
        for i in range(l, r+1):
            arr[l], arr[i] = arr[i], arr[l]
            permute(arr, l+1, r)
            arr[i], arr[l] = arr[l], arr[i]

def permutations_recursion(ip, op, res, d):
    if len(ip) == 0:
        res.append(op)
        return
    d = dict()
    for i in range(len(ip)):
        if d.get(ip[i], None) is None:
            d[ip[i]] = 0
            newIp = ip[:i] + ip[i+1:]
            newOp = op + [ip[i]]
            permutations_recursion(newIp, newOp, res, d)

def swap(a, i, j):
    return a[:i]+a[j]+a[i+1:j]+a[i]+a[j+1:]

def findMaximumNum(num, k, maxm):
    # base condition
    if k == 0:
        return
    lNum = len(num)
    for i in range(lNum-1):
        for j in range(i+1, lNum):
            if num[i] < num[j] and num[j] >= max(num[j:]):
                num = swap(num, i, j)
                if maxm[0] < num:
                    maxm[0] = num
                findMaximumNum(num, k-1, maxm)
                num = swap(num, i, j)

# https://leetcode.com/problems/subsets
def subsets(nums, start, end, tmp, res):
    res.append(tmp[:])
    for i in range(start, end):
        tmp.append(nums[i])
        subsets(nums, i+1, end, tmp, res)
        tmp.pop()

if __name__ == "__main__":
    s = "abc"
    l = list(s)
    lens = len(s)
    permute(l, 0, lens-1)
    print()

    a = [1,1,2]
    res = list()
    permutations_recursion(a, [], res, dict())
    print(res)

    num = "4577"
    k = 4
    maxm = ["0"]
    findMaximumNum(num, k, maxm)
    print(maxm[0])

    nums = [1,2,3]
    res = []
    subsets(nums, 0, len(nums), [], res)
    print(res)
