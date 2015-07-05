'''Implement Grpah ADT traversal in python
BFS (Breadth-First-Search) and DFS (Depth-First-Search)
@Inp:

  ,--->A
  |   / \
  |  B   C
  |  |\ /|
  |  | D |
  |  | | |
  |  '-E-'
  '----'
'''

# def depth_first_search(graph, start, path=[]):
# 	'''Recursice dfs from start node'''
# 	path.append(start)
# 	for node in graph[start]:
# 		if not node in path:
# 			print path
# 			depth_first_search(graph, node, path)
# 	return path

def depth_first_search(graph, start, path=[]):
	'''Recursice dfs from start node'''
	q = [start]
	while q:
		v = q.pop()
		if not v in path:
			print path
			path.append(v)
			q += graph[v]
	return path

def breadth_first_search(graph, start, path=[]):
	'''Iterative bfs from start node'''
	q = [start]
	while q:
		v = q.pop(0)
		if not v in path:
			print path
			path.append(v)
			q += graph[v]
	return path


if __name__ == "__main__":
	graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['D', 'E'], 'D': ['E'], 'E': ['A']}
	start = 'A'
	print depth_first_search(graph, start)
	print "*"*80
	print breadth_first_search(graph, start)
