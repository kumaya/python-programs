# Given an array, print the Next Greater Element (NGE) for every element. 
#The Next greater Element for an element x is the first greater element on the right side of x in array. 
#Elements for which no greater element exist, consider next greater element as -1.

def nextGreaterElement(inp_arr):
	out_list = []
	len_inp = len(inp_arr)
	for i in xrange(1, len_inp):
		count = i
		out_list.append(inp_arr[i-1])
		next = inp_arr[i]
		while len(out_list) > 0:
			popped_elem = out_list.pop()
			if next > popped_elem:
				print str(next) + " is next greater element of " + str(popped_elem)
			else:
				if count < len_inp:
					out_list.append(popped_elem)
					next = inp_arr[count]
					count += 1
				else:
					print "-1 is next greater element of " + str(popped_elem)


inp_arr = [4,5,2,25]
inp_arr1 = [13,7,6,12]
nextGreaterElement(inp_arr1)
print "*"*80
nextGreaterElement(inp_arr)