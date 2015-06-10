 
# Find longest path in a maze
def findLongestPath1(inp_mat, start, end):
	result = []
	rows = len(inp_mat)
	cloumns = len(inp_mat[0])
	if inp_mat[start[0]][start[1]] == 0:
		return 0
	elif start == end:
		path = []
		path.append(start)
		return path
	

def findLongestPath(inp_mat):
	start = (0,0)
	end = (len(inp_mat)-1, len(inp_mat[0])-1)
	path = findLongestPath1(inp_mat, start, end)
	return path


if __name__ == "__main__":
	inp_mat = [[1,1,1,1,0,0,1,0,1,0],
	           [0,0,0,1,0,0,1,0,0,1],
    	       [1,1,1,1,0,0,1,1,1,1],
        	   [1,1,1,1,0,1,1,0,1,1],
	           [1,1,1,1,0,1,0,1,0,1],
    	       [0,1,1,1,1,1,1,0,0,1],
        	   [1,0,0,1,0,1,1,0,1,0],
	           [1,0,1,0,0,1,0,1,1,1],
    	       [1,1,1,0,0,1,1,0,1,1],
        	   [0,0,1,1,0,0,1,1,1,1]]

	longest_path = findLongestPath(inp_mat)
	if longest_path == 0:
		print "No Path possible"
	else:
		print longest_path

