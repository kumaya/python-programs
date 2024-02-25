# Given an array, print the Next Greater Element (NGE) for every element. 
#The Next greater Element for an element x is the first greater element on the right side of x in array. 
#Elements for which no greater element exist, consider next greater element as -1.

def nextGreaterElement(inp_arr):
	for i in range(len(inp_arr)-1):
		for j in range(i, len(inp_arr)):
			flag = False
			if inp_arr[j] > inp_arr[i]:
				flag = True
		if flag:
			print("%s is the next greater element of %s" % (inp_arr[j], inp_arr[i]))
		else:
			print("-1 is the next greater element of %s" %(inp_arr[i]))

def nge(a):
	res = [-1] * len(a)
	stack = list()
	for i in range(len(a)-1, -1, -1):
		while len(stack) > 0 and stack[-1] < a[i]:
			stack.pop()
		if len(stack) != 0:
			res[i] = stack[-1]
		stack.append(a[i])
	return res

inp_arr = [4,5,2,25]
inp_arr1 = [13,7,6,12]
nextGreaterElement(inp_arr1)
print("*"*80)
nextGreaterElement(inp_arr)
print("*"*80)
print(nge(inp_arr1))
print(nge(inp_arr))


def nsm(a):
	invs = 0
	res = [-1] * len(a)
	stack = list()
	for i in range(len(a)-1, -1, -1):
		while len(stack) > 0 and stack[-1] > a[i]:
			stack.pop()
		if len(stack) > 0:
			# invs = 1 + stack[-1][1]
			res[i] = stack[-1]
		stack.append(a[i])
	return invs

a = [2,4,1,3,5]
print(nsm(a))