import Stack
from copy import deepcopy


class Graph:
    def __init__(self, size):
        self.adjacency_matrix = [[None] * (size + 1) for _ in range(size + 1)]
        self.size = size

    def insert(self, vertex1, vertex2, edge_value):
        if vertex1 < 0 or vertex2 < 0 or vertex1 > self.size or vertex2 > self.size:
            raise Exception("Vertex number must be non-begative and less than graph size")
        elif edge_value <= 0:
            raise Exception("Edge value must be positive")
        elif self.adjacency_matrix[vertex1][vertex2] is None:
            self.adjacency_matrix[vertex1][vertex2] = edge_value
        else:
            raise Exception("Edge already exists")

    def remove(self, vertex1, vertex2):
        if vertex1 < 0 or vertex2 < 0 or vertex1 > self.size or vertex2 > self.size:
            raise Exception("Vertex number must be non-negative and less than graph size")
        elif self.adjacency_matrix[vertex1][vertex2] is None:
            raise Exception("Edge does not exist")
        else:
            self.adjacency_matrix[vertex1][vertex2] = None

    def ford_fulkerson(self, source, end):
        if source < 0 or end < 0 or source > self.size or end > self.size:
            raise Exception("Source and end vertex numbers must be non-negative and less than graph size")
        if source == end:
            return 0
        closed = [False] * (self.size + 1) # If True then vertex is closed
        temp_graph = deepcopy(self.adjacency_matrix) 
        max_flow = 0 
        cur_path = Stack.Stack() # Current path
        cur_path.push(source) # Add source to current path
        path_exists = True
        while path_exists: # While path from source to end exists
            cur = None # Current vertex
            cur_min_edge = None # Current minimal edge in path
            for i in range(self.size + 1): # Find open adjacenct vertex to source vertex
                if temp_graph[source][i] is not None and closed[i] == False and temp_graph[source][i] > 0:
                    cur = i
                    if cur_min_edge is None or temp_graph[source][i] < cur_min_edge: # Update minimal edge if needed
                        cur_min_edge = temp_graph[source][i]
                    break
            if cur is None: # If there is no open adjacent vertex
                path_exists = False # Path from source to end no longer exists
                break
            while cur != end: # While path to end is not found
                cur_path.push(cur) # Push current vertex to path
                temp = cur 
                cur = None
                for i in range(self.size + 1): # Find open adjacent vertex to current vertex
                    if temp_graph[temp][i] is not None and closed[i] == False and temp_graph[temp][i] > 0:
                        cur = i
                        if cur_min_edge is None or temp_graph[temp][cur] < cur_min_edge: # Update minimal edge if needed
                            cur_min_edge = temp_graph[temp][cur]
                        break
                if cur is None: # If there is no open adjacent vertex
                    cur_path.pop() 
                    closed[temp] = True # Close current vertex
                    while not cur_path.isEmpty(): # Close previous vertexes in path if they need closing
                        for i in range(self.size + 1):
                            if temp_graph[cur_path.top()][i] is not None and closed[i] == False and temp_graph[cur_path.top()][i] > 0: # If open adjacent vertex found
                                cur_path.clear() # Clear current path
                                break # End for loop
                        else: # If open adjacent vertex not found in for loop
                            closed[cur_path.top()] = True # Close current vertex
                            cur_path.pop() # Delete current vertex from current path
                    cur_path.push(source) # Push source vertex to current path
                    break # Go back to start
            if cur is not None: # If path to end vertex found
                cur_path.push(cur) # Add current vertex to path
                if cur_min_edge is None or temp_graph[temp][cur] < cur_min_edge: # Update minimal edge if needed
                    cur_min_edge = temp_graph[temp][cur]
                max_flow += cur_min_edge # Update max_flow
                while cur_path.top() != source: # Update all edges in path
                    cur = cur_path.pop()
                    temp_graph[cur_path.top()][cur] -= cur_min_edge
                cur_min_edge = None # Reset minimal edge
        return max_flow # Return max_flow
