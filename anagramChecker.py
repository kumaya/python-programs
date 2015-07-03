# Program to check if two given strings are anagram in O(n) time

# Method 1
def anagramChecker(str1, str2):
	lst1 = [0] * 26
	lst2 = [0] * 26

	for i in xrange(len(str1)):
		pos = ord(str1[i]) - ord('a')
		lst1[pos] = lst1[pos] + 1

	for i in xrange(len(str2)):
		pos = ord(str2[i]) - ord('a')
		lst2[pos] = lst2[pos] + 1

	j = 0
	is_cool = True
	while  j<26 and is_cool:
		if lst1[j] == lst2[j]:
			j += 1
		else:
			is_cool = False

	return is_cool


# Method 2
from collections import Counter
def checkerUsingCounter(str1, str2):
	if Counter(str1) == Counter(str2):
		return True
	else:
		return False

# Method 3
def checkerUsingOrd(str1, str2):
	sum1 = sum([ord(i) for i in str1])
	sum2 = sum([ord(i) for i in str2])
	if sum1 == sum2:
		return True
	else:
		return False

# Method 4
def checkerUsingList(str1, str2):
	out_list1 = []
	out_list2 = []
	inp_lst1 = list(str1)
	for i in inp_lst1:
		if 122 >= ord(i.lower()) >= 97:
			out_list1.append(i.lower())
	
	inp_lst2 = list(str2)
	for i in inp_lst2:
		if 122 >= ord(i.lower()) >= 97:
			out_list2.append(i.lower())
	if sorted(out_list1) == sorted(out_list2):
		return True
	else:
		return False

if __name__ == "__main__":
	str1 = 'kuchbhi'
	str2 = 'bukihch'
	print "Using normal logic: ", anagramChecker(str1, str2)
	print "Using Counter: ", checkerUsingCounter(str1, str2)
	print "Using ord: ", checkerUsingOrd(str1, str2)
	print "Using list: ", checkerUsingList(str1, str1)

	# Calculate running time for all methods
	from timeit import Timer
	t1 = Timer("anagramChecker('kuchbhi', 'bukihch')", "from __main__ import anagramChecker")
	print "time taken using anagramChecker: ", t1.timeit(number=10000), "ms"

	t2 = Timer("checkerUsingCounter('kuchbhi', 'bukihch')", "from __main__ import checkerUsingCounter")
	print "time taken using checkerUsingCounter: ", t2.timeit(number=10000), "ms"

	t3 = Timer("checkerUsingOrd('kuchbhi', 'bukihch')", "from __main__ import checkerUsingOrd")
	print "time taken using checkerUsingOrd: ", t3.timeit(number=10000), "ms"

	t4 = Timer("checkerUsingList('kuchbhi', 'bukihch')", "from __main__ import checkerUsingList")
	print "time taken using checkerUsingList: ", t4.timeit(number=10000), "ms"