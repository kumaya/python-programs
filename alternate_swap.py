"""
An array contains both positive and negative numbers in random order.
Rearrange the array elements so that positive and negative numbers are placed alternatively.
Number of positive and negative numbers need not be equal.
If there are more positive numbers they appear at the end of the array.
If there are more negative numbers, they too appear in the end of the array.
"""


def rearrange(inp, li):
    # Sort array so that all negative nos. gets arranged to one side while positive nos to other
    j = 0
    for i in range(1, li):
        if inp[i] < 0:
            j += 1
            swap(i, inp, j)
    pos = j+1
    neg = 0
    while pos < li and neg < li and inp[neg] < 0:
        swap(pos, inp, neg)
        pos += 1
        neg += 2
    return inp


def swap(i, inp, j):
    inp[j] = inp[j] ^ inp[i]
    inp[i] = inp[j] ^ inp[i]
    inp[j] = inp[j] ^ inp[i]


if __name__ == "__main__":
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9, -2, -4, -5, -6]
    l = len(arr)
    print arr
    print rearrange(arr, l)