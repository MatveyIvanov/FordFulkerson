import Graph

def file_len(filename): # Number of lines in file
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

with open('graph.txt', 'r') as f:
    graph = Graph.Graph(file_len('graph.txt') - 1)
    source, end = None, None
    for line in f: # Loop through all lines
        line = line.strip('\n') # Delete \n symbol from line
        line = line.strip('\r') # Delete \r symbol from line
        line = line.split(' ') # Slpit line by spaces
        if source is None:
            source, end = int(line[0]), int(line[1])
        else:
            graph.insert(int(line[0]), int(line[1]), int(line[2]))

print(graph.ford_fulkerson(source, end))

