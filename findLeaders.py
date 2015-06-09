#input: random array
#output: leaders; a number is a leader if all numbers following it are less then it

def findLeaders(inp_arr):
	out_list = []
	len_inp_arr = len(inp_arr)
	start = inp_arr[len_inp_arr-1]
	out_list.append(inp_arr[len_inp_arr-1])
	for i in xrange(len_inp_arr):
		if start < inp_arr[len_inp_arr-1-i]:
			start = inp_arr[len_inp_arr-1-i]
			out_list.append(start)
	return out_list

inp_arr = [9,4,3,18,2,1,5,4,1]
print findLeaders(inp_arr)