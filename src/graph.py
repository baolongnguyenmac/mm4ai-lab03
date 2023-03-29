from vertex import Vertex
from support import get_log


class Graph:
    def __init__(self):
        """
        Module constructing Graph class.
        """
        self.vertList: dict[int, Vertex] = {}
        self.numVertices = 0

    def addVertex(self, key):
        """
        Module adding a vertex to Graph.

        :param key: vertex `key`
        :return: `key` as Vertex class
        """
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        """
        Module returning Vertex `n` of Graph.

        :param n: the input vertex name `n`.
        :return: None if not exist else return Vertex `n`
        """
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        """
        Module to determine does vertex `n` belonged to Graph.

        :param n: vertex `n`.
        :return: True if belonged to Graph else False.
        """
        return n in self.vertList

    def addEdge(self, f, t, weight=1):
        """
        Module adding an Edge to Graph.

        :param f: the beginning vertex.
        :param t: the ending vertex.
        :param weight: the weight of that Edge.
        :return:
        """
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        """
        Module to get list vertex name of Graph.
        :return: list of vertex name.
        """
        return self.vertList.keys()

    def __iter__(self):
        """
        Module for looping with the vertices adjacency of each Vertex in Graph.
        :return: list adjacency of each vertex.
        """
        return iter(self.vertList.values())

    @classmethod
    def build_graph_from_file(cls, filename, delimiter=" "):
        """ Module is used for building graph from file
        :param filename: the directory to filename
        :return: graph
        """
        g = cls()
        for line in open(filename, 'U'):
            L = line.strip().split(delimiter)
            if (L[0] not in g.getVertices()):
                g.addVertex(L[0])
            for i in range(1, len(L)):
                if (L[i] not in g.getVertices()):
                    g.addVertex(L[i])
                g.addEdge(L[0], L[i])
        return g

    @classmethod
    def build_graph_from_edge_list(cls, d):
        """ Module is used for building graph from edge list
        :param d: the edge list
        :return: graph
        """
        g = cls()
        for v1, v2_list in d.items():
            if (v1 not in g.getVertices()):
                g.addVertex(v1)
            for v2 in v2_list:
                if (v2 not in g.getVertices()):
                    g.addVertex(v2)
                g.addEdge(v1, v2)

        return g

    def BFS(self, vertex_ith: int):
        """
        Module applying Breadth First Search Algorithm.

        :param vertex_ith: the vertex id in Graph
        :return: path computed by BFS
        """
        vertex = self.getVertex(vertex_ith)  # get the vertex `vertex_ith`.
        if not vertex:  # checking if not exist `vertex_ith` in Graph then raise error
            message = 'Invalid vertex id, could not found vertex id `' + \
                str(vertex_ith) + '` in Graph'
            raise ValueError(get_log(message, log_type='ERROR'))
        n = self.numVertices  # get the number of vertices.
        visited = [False] * n  # bool array for marking visited or not.
        vertex_id = vertex.getId()  # get the vertex_id for easy management.
        # initializing a queue to handling which vertex is remaining.
        queue = [vertex_id]
        # marking the `vertex_id` is visited due to the beginning vertex.
        visited[vertex_id] = True
        path = []  # path to track the working state of BFS.
        while queue:
            # handling current vertex before removing out of queue.
            cur_pos = queue[0]
            path.append(cur_pos)  # appending to path to track.
            queue.pop(0)  # remove it out of queue
            neighbor_cur_pos = [x.id for x in self.getVertex(
                cur_pos).getConnections()]  # get all neighbors id of
            # current vertex.
            for neighborId in neighbor_cur_pos:  # loop over the neighbor of current vertex.
                # if not visited then push that vertex into queue.
                if not visited[neighborId]:
                    visited[neighborId] = True
                    queue.append(neighborId)
        return path

    def DFS(self, vertex_ith: int, visited=None):
        """depth first search function, start from `vertex_ith`
        Args:
            vertex_ith (int): key of vertex in graph
        Raises:
            ValueError: can't find a vertex with given key
        Returns:
            list[int]: the path that DFS agent has gone through
        """
        vertex: Vertex = self.getVertex(vertex_ith)
        if vertex is None:
            message = 'Invalid vertex id, could not found vertex id `' + \
                str(vertex_ith) + '` in Graph'
            raise ValueError(get_log(message, log_type='ERROR'))

        closed_set: list[int] = []
        open_set: list[int] = [vertex.getId()]

        while open_set:
            cur_vertex: Vertex = self.getVertex(open_set.pop())
            cur_vertex_id = cur_vertex.getId()

            if cur_vertex_id not in closed_set:
                closed_set.append(cur_vertex_id)
                if (visited is not None):
                    visited.append(cur_vertex_id)
                neighbors = [x.id for x in cur_vertex.getConnections()]

                for neighbor in neighbors:
                    if (visited is not None):
                        if (neighbor not in closed_set) & (neighbor not in visited):
                            open_set.append(neighbor)
                    else:
                        if (neighbor not in closed_set):
                            open_set.append(neighbor)

        return closed_set

    def get_transpose(self):
        """ Module is used for building graph from edge list
        :param d: the edge list
        :return: graph
        """
        g = Graph()
        for i in self.vertList.keys():
            for j in self.getVertex(i).getConnections():
                g.addEdge(j.id, i)
        return g

    def FillOrder(self, vertex_ith: int, visited, stack):
        """ Module is used for get vertex list obey depth first traversal
        :param vertex_ith: int, visited list, and stack
        """
        # Mark the current node as visited
        vertex: Vertex = self.getVertex(vertex_ith)
        if vertex is None:
            message = 'Invalid vertex id, could not found vertex id `' + \
                str(vertex_ith) + '` in Graph'
            raise ValueError(get_log(message, log_type='ERROR'))
        visited.append(vertex_ith)

        # Recur for all the vertices adjacent to this vertex
        for i in vertex.getConnections():
            if i.id not in visited:
                self.FillOrder(i.id, visited, stack)
        stack = stack.append(vertex_ith)

    def Find_SCC_by_Kosaraju(self):
        """ Module is used for find strong connect components by Kosaraju's algorithm.
        :param start_node
        :return strong connect components (SCCs)
        """
        SCCs = {}
        # Step 1: DFS
        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited = []
        # Fill vertices in stack according to their finishing
        # times
        for i in self.getVertices():
            if i not in visited:
                self.FillOrder(i, visited, stack)
        # Step 2: Get graph's transpose
        g_T = self.get_transpose()
        # Step 3: Get DFS again
        visited = []
        index = 0
        while stack:
            i = stack.pop()
            if i not in visited:
                index += 1
                scc = g_T.DFS(i, visited)
                SCCs[index] = scc

        return SCCs
