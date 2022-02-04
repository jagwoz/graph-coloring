from graph import *
import copy
import numpy as np


class graph_generator:
    def __init__(self, percent):
        self.adjacency = []
        self.percent = percent

    def get_graph(self, adj):
        self.adjacency = adj
        return graph(adjacency=self.adjacency)

    def next_graph(self, n):
        def is_consistent(new_adjacency):
            n = len(new_adjacency)
            checked = [1] + [0] * (n - 1)
            checked_s = [0] * n
            iter = 0

            while sum(checked_s) < n and iter < n:
                iter += 1
                neighbors = []
                for i in range(len(checked)):
                    if checked[i] == 1:
                        checked_s[i] = 1
                        for j in range(len(new_adjacency[i])):
                            if new_adjacency[i][j] == 1:
                                neighbors.append(j)
                                checked[j] = 1
                        if sum(checked_s) == n:
                            return True
            return False

        self.adjacency = []
        for i in range(n):
            v_neighbors = []
            for j in range(n):
                if j == i:
                    v_neighbors.append(0)
                else:
                    v_neighbors.append(1)
            self.adjacency.append(v_neighbors)

        edges = []
        for i in range(n):
            for j in range(n):
                if not [i, j] in edges and not [j, i] in edges and self.adjacency[i][j] == 1:
                    edges.append([i, j])
        all_edges = len(edges)
        edges_max = all_edges
        while len(edges) > self.percent * edges_max:
            adjacency_temp = copy.deepcopy(self.adjacency)
            random_edge = int(np.random.uniform(0, len(edges)))
            u, v = edges[random_edge][0], edges[random_edge][1]
            if not adjacency_temp[u][v] == 0:
                adjacency_temp[u][v] = 0
                adjacency_temp[v][u] = 0

                if is_consistent(adjacency_temp):
                    self.adjacency = adjacency_temp.copy()
                    all_edges -= 1
                if [u, v] in edges:
                    edges.remove([u, v])
                else:
                    edges.remove([v, u])
        return graph(adjacency=self.adjacency)