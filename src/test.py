from graph import Graph
from algorithms import KL

g = Graph()
for i in range(8):
    g.addVertex(i)

g.addEdge(0, 1, 2)
g.addEdge(1, 0, 2)

g.addEdge(0, 3, 5)
g.addEdge(3, 0, 5)

g.addEdge(1, 2, 3)
g.addEdge(2, 1, 3)

g.addEdge(1, 4, 1)
g.addEdge(4, 1, 1)

g.addEdge(2, 5, 1)
g.addEdge(5, 2, 1)

g.addEdge(2, 3, 4)
g.addEdge(3, 2, 4)

g.addEdge(4, 6, 6)
g.addEdge(6, 4, 6)

g.addEdge(4, 5, 9)
g.addEdge(5, 4, 9)

g.addEdge(5, 7, 7)
g.addEdge(7, 5, 7)

g.addEdge(6, 7, 8)
g.addEdge(7, 6, 8)

# output:
#     [1, 5, 2, 7] [0, 3, 4, 6] 24
#     [1, 2, 4, 5] [0, 3, 6, 7] 19 (local minimum)
# or:
#     [4, 1, 3, 0] [2, 5, 6, 7] 22
#     [0, 1, 2, 3] [4, 5, 6, 7] 2 (global minimum)
kl = KL(g)
kl.partition()

