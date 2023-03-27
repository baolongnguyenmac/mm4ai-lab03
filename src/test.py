from graph import Graph
from support import save_path

# main
g = Graph()
for i in range(6):
    g.addVertex(i)
g.addEdge(0, 1, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 4, 7)
g.addEdge(3, 5, 3)
g.addEdge(4, 0, 1)
g.addEdge(5, 4, 8)
g.addEdge(5, 2, 1)
# for v in g:
#     for w in v.getConnections():
#         print("( %s , %s )" % (v.getId(), w.getId()))

# test BFS and write mode
path_bfs = g.BFS(0)
path_dfs = g.DFS(0)
save_path(path_bfs, mode='write_to_file', file_name='output_bfs.txt')
save_path(path_dfs, mode='write_to_file', file_name='output_dfs.txt')
