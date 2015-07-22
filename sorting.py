""" Bubble sort: The bubble sort makes multiple passes through a list.
It compares adjacent items and exchanges those that are out of order.
Each pass through the list places the next largest value in its proper place.
"""

def bubble_sort(inp_list):
    for i in range(len(inp_list)-1, 0, -1):
        for j in range(i):
            if inp_list[j] > inp_list[j+1]:
                temp = inp_list[j]
                inp_list[j] = inp_list[j+1]
                inp_list[j+1] = temp
    return inp_list


""" Selection sort: selection sort looks for the largest value as it makes a
pass and, after completing the pass, places it in the proper location.
"""

def selection_sort(inp_list):
    for i in range(len(inp_list)-1, 0, -1):
        pos_of_max = 0
        for j in range(1, i+1):
            if inp_list[j] > inp_list[pos_of_max]:
                pos_of_max = j
        temp = inp_list[i]
        inp_list[i] = inp_list[pos_of_max]
        inp_list[pos_of_max] = temp
    return inp_list


""" Insertion Sort: It always maintains a sorted sub list in the lower positions of
the list. Each new item is then inserted back into the previous sub list such that
the sorted sub list is one item larger
"""

def insertion_sort(inp_list):
    for i in range(1, len(inp_list)):
        current_val = inp_list[i]
        position = i
        while position > 0 and inp_list[position-1] > current_val:
            inp_list[position] = inp_list[position - 1]
            position -= 1
        inp_list[position] = current_val
    return  inp_list


""" Merge sort
"""
def merge_sort(inp_list):
    if len(inp_list) > 1:
        mid = len(inp_list) // 2
        left_half = inp_list[:mid]
        right_half = inp_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                inp_list[k] = left_half[i]
                i += 1
            else:
                inp_list[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            inp_list[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            inp_list[k] = right_half[j]
            j += 1
            k += 1
    return inp_list


""" Quick sort
"""
import random
def quick_sort(inp_list):
    if len(inp_list) < 1:
        return inp_list
    else:
        pivot = random.randint(0, len(inp_list)-1)
        pivot_ele = inp_list[pivot]
        return (quick_sort([x for x in inp_list if x < pivot_ele]) +
                [x for x in inp_list if x == pivot_ele] +
                quick_sort([x for x in inp_list if x > pivot_ele]))


from random import randint
inp_list = [randint(-2, i) for i in range(10)]
print "Bubble sort:", bubble_sort(inp_list)
inp_list = [randint(-2, i) for i in range(10)]
print "Selection sort:", selection_sort(inp_list)
inp_list = [randint(-2, i) for i in range(10)]
print "Insertion sort:", insertion_sort(inp_list)
inp_list = [randint(-2, i) for i in range(10)]
print "Merge sort:", merge_sort(inp_list)
inp_list = [randint(-2, i) for i in range(10)]
print "Quick sort:", quick_sort(inp_list)

print "*"*56
print("Let's check the running time of these sorting techniques")
print "*"*56
import timeit
from timeit import Timer

inp_list1 = [randint(-10000, 10000) for i in range(1000)]
qs = Timer("quick_sort(inp_list1)", "from __main__ import quick_sort, inp_list1")
print "time taken for quick_sort: ", qs.timeit(number=1000), "ms"

inp_list2 = [randint(-10000, 10000) for i in range(1000)]
ms = Timer("merge_sort(inp_list2)", "from __main__ import merge_sort, inp_list2")
print "time taken for merge_sort: ", qs.timeit(number=1000), "ms"

inp_list3 = [randint(-10000, 10000) for i in range(1000)]
inss = Timer("insertion_sort(inp_list3)", "from __main__ import insertion_sort, inp_list3")
print "time taken for insertion_sort: ", inss.timeit(number=1000), "ms"

inp_list4 = [randint(-10000, 10000) for i in range(1000)]
ss = Timer("selection_sort(inp_list4)", "from __main__ import selection_sort, inp_list4")
print "time taken for selection_sort: ", ss.timeit(number=1000), "ms"

inp_list5 = [randint(-10000, 10000) for i in range(1000)]
bs = Timer("bubble_sort(inp_list5)", "from __main__ import bubble_sort, inp_list5")
print "time taken for bubble_sort: ", bs.timeit(number=1000), "ms"
