from support import *


class Vertex:
    def __init__(self, key):
        """
        Module for initializing Vertex class.

        :param key: identifying vertex id by key.
        """
        self.id = key  # assigning `id` attribute by the input `key`.
        self.connectedTo = {}  # handling which vertex is connected with this vertex.
        self.group = ''

    def get_diff_cost(self):
        internal_cost, external_cost = 0, 0
        for node in self.connectedTo.keys():
            if node.group == self.group:
                internal_cost += self.connectedTo[node]
            else:
                external_cost += self.connectedTo[node]
        return external_cost - internal_cost

    def addNeighbor(self, nbr, weight=0):
        """
        Module adding neighbor for Vertex.
        :param nbr: Vertex neighbor having connection with this vertex.
        :param weight: the weight of edge between this vertex and vertex `nbr`.
        :return:
        """
        self.connectedTo[nbr] = weight

    def __str__(self):
        """
        Module for show the information of vertex.

        :return: vertex id and its neighbors.
        """
        return str(self.id) + " connectedTo: " + str([x.id for x in self.connectedTo])

    def getConnections(self):
        """
        Module getting all neighbors of this vertex.

        :return: dict_keys() which saving all neighbors of this vertex.
        """
        return self.connectedTo.keys()

    def getId(self):
        """
        Module getting the `id` of this vertex.

        :return: `id` of this vertex.
        """
        return self.id

    def getWeight(self, nbr):
        """
        Module getting weight of connection between this vertex and vertex `nbr`.

        :param nbr: vertex has connection with this vertex.
        :return: weight of edge.
        """
        return self.connectedTo[nbr]
