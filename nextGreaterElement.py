# Given an array, print the Next Greater Element (NGE) for every element. 
#The Next greater Element for an element x is the first greater element on the right side of x in array. 
#Elements for which no greater element exist, consider next greater element as -1.

def nextGreaterElement(inp_arr):
	for i in xrange(len(inp_arr)-1):
		for j in xrange(i, len(inp_arr)):
			flag = False
			if inp_arr[j] > inp_arr[i]:
				flag = True
		if flag:
			print "%s is the next greater element of %s" % (inp_arr[j], inp_arr[i])
		else:
			print "-1 is the next greater element of %s" %(inp_arr[i])


inp_arr = [4,5,2,25]
inp_arr1 = [13,7,6,12]
nextGreaterElement(inp_arr1)
print "*"*80
nextGreaterElement(inp_arr)