from graph import Graph
import random

# Kernighan–Lin_algorithm (using undirected graph)
# ref: https://github.com/BrianMburu/Kernighan-Lin-Algorithm/blob/master/kl.py
# ref: https://patterns.eecs.berkeley.edu/?page_id=571#1_BFS
class KL:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph

        n = len(self.graph.vertList)
        self.group_a = random.sample(sorted(self.graph.vertList), k=n//2)
        self.group_b = list(set(self.graph.vertList.keys()) - set(self.group_a))

        for i in self.group_a:
            self.graph.vertList[i].group = 'A'
        for i in self.group_b:
            self.graph.vertList[i].group = 'B'

        print(self.group_a, self.group_b, self.partition_cost())

    def cost(self, node1: int, node2: int):
        try:
            return self.graph.vertList[node1].connectedTo[self.graph.vertList[node2]]
        except KeyError:
            return 0

    def partition_cost(self):
        cost = 0
        for node1 in self.group_a:
            for node2 in self.group_b:
                cost += self.cost(node1, node2)
        return cost

    def partition(self):
        total_gain = 0
        for _ in range(len(self.graph.vertList)//2):
            D_values = {v: self.graph.vertList[v].get_diff_cost() for v in self.graph.vertList.keys()}

            gains = []

            for a in self.group_a:
                for b in self.group_b:
                    c_ab = self.cost(a, b)
                    gain = D_values[a] + D_values[b] - 2*c_ab
                    gains.append(([a, b], gain))

            gains = sorted(gains, key=lambda x: x[1], reverse=True)
            max_gain = gains[0][1]
            if max_gain <= 0:
                return self.group_a, self.group_b, self.partition_cost()

            pair = gains[0][0]
            self.group_a.remove(pair[0])
            self.group_b.remove(pair[1])
            self.graph.vertList[pair[0]].group = "B"
            self.graph.vertList[pair[1]].group = "A"

            self.group_a = [key for key in self.graph.vertList.keys() if self.graph.vertList[key].group == 'A']
            self.group_b = [key for key in self.graph.vertList.keys() if self.graph.vertList[key].group == 'B']
            print(self.group_a, self.group_b, self.partition_cost())

            for x in self.group_a:
                c_xa = self.cost(x, pair[0])
                c_xb = self.cost(x, pair[1])
                D_values[x] += 2 * c_xa - 2 * c_xb

            for y in self.group_b:
                c_yb = self.cost(y, pair[1])
                c_ya = self.cost(y, pair[0])
                D_values[y] += 2 * c_yb - 2 * c_ya

			# Update the total gain.
            total_gain += max_gain

        print(f'Partition cost: {self.partition_cost()}')
        print(self.group_a, self.group_b)
        return self.group_a, self.group_b, self.partition_cost()
