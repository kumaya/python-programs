# 2D array in python
matix = [[x for x in xrange(5)] for _ in xrange(5)]
print matix[1][2]

print "*"*80
# Maximum subsequence of 0's in a binary number
bin_num = 1000000011111010110001
bin_num = int(str(bin_num), 2)
print bin_num
maxLen = 0
currLen = 0
while bin_num > 0:
	if bin_num%2 == 1:
		currLen = 0
	else:
		currLen += 1
	if currLen > maxLen:
		maxLen = currLen
	bin_num = bin_num/2
print maxLen

print "*"*80
# Maximum size square sub-matrix with all 1's
inp_mat = [[1, 1, 1, 0, 1],			
           [1, 1, 0, 1, 0],
           [0, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [0, 0, 0, 0, 0]]
max_val = 0
for i in xrange(len(inp_mat)):
	for j in xrange(len(inp_mat[0])):
		if inp_mat[i][j] == 1:
			inp_mat[i][j] = min(inp_mat[i][j-1], inp_mat[i-1][j], inp_mat[i-1][j-1]) + 1
		else:
			inp_mat[i][j] = 0
for i,j  in enumerate(inp_mat):
	for k, l in enumerate(inp_mat[i]):
		if l > max_val:
			max_val = l
print "Maximum size square is %d" %(max_val)
