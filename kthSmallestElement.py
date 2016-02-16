# Given an unsorted list. Find k'th smallest element in list
import random


def QuickSelect(inp_arr, k, len_arr):
    p = random.randint(0, len_arr - 1)
    A1 = []
    A2 = []
    p = inp_arr[p]
    for i in xrange(0, len_arr):
        if inp_arr[i] < p:
            A1.append(inp_arr[i])
        if inp_arr[i] > p:
            A2.append(inp_arr[i])
    if len(A1) >= k:
        return QuickSelect(A1, k, len(A1))
    if (len_arr - len(A2)) < k:
        return QuickSelect(A2, k - (len_arr - len(A2)), len(A2))
    else:
        return p


inp_arr = [3, 4, 13, 10, 11, 34, 9, 15]
len_arr = len(inp_arr)
k = 3
value = QuickSelect(inp_arr, k, len_arr)
print value
