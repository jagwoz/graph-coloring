class graph:
    def __init__(self, adjacency):
        def update_neighbors():
            def is_incidence(i, j):
                if self.adjacency[i][j] == 1:
                    return True
                return False

            for i in range(self.n):
                is_neighbor = []
                for j in range(self.n):
                    if is_incidence(i, j):
                        is_neighbor.append(j)
                self.neighbors.append(is_neighbor)

        self.adjacency = adjacency
        self.n = len(adjacency)
        self.neighbors = []
        update_neighbors()

    def get_n(self):
        return self.n

    def get_adjacency(self):
        return self.adjacency

    def get_neighbors(self, i):
        return self.neighbors[i]

    def get_degree(self, i):
        return sum(self.adjacency[i])

    def get_max_degree(self):
        max_degree = sum(self.adjacency[0])
        for i in range(1, self.n):
            if sum(self.adjacency[i]) > max_degree:
                max_degree = sum(self.adjacency[i])
        return max_degree
