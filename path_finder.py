import math

def find_():
	start = (0,0)
	end = (4,0)
	cost = 1
	open_set = {start}
	cost_so_far = {start: 0}
	came_from = {}
	path = None
	while open_set:

		current = min(open_set, key=lambda node: cost_so_far[node] + heuristic(node, end))
		open_set.remove(current)


		if current == end: break
		for neighbor in get_neighbors(current, grid):
			new_cost = cost_so_far[current] + cost
			if ((neighbor not in cost_so_far or new_cost < cost_so_far[neighbor] )and grid[neighbor[0]][neighbor[1]]==0):
				cost_so_far[neighbor] = new_cost
				came_from[neighbor] = current
				open_set.add(neighbor)

	if end not in came_from:
		print("No path found")
	else:
		path = [end]
		while path[-1] != start:
			path.append(came_from[path[-1]])
		path.reverse()
	return (path)


def heuristic(a, b):
	return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
	
def get_neighbors(point,matrix):
	neighbors = []
	m = len(matrix) 
	n = len(matrix[0]) 
	x, y = point 
	for i in range(x - 1, x + 2): 
		for j in range(y - 1, y + 2): 
			if (0 <= i < m) and (0 <= j < n): 
				neighbors.append((i, j)) 
	return neighbors

grid = {"1":[[0, 0, 0, 0, 0],
			[1, 1, 1, 1, 0],
			[0, 0, 1, 0, 0],
			[0, 1, 1, 1, 0],
			[0, 0, 0, 0, 0]]

		}