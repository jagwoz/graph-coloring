class algorithm_exact:
    def __init__(self, graph):
        self.graph = graph
        self.n = graph.get_n()
        self.b = 2
        self.ct = [0] * self.n

    def get_b(self):
        return self.b

    def get_ct(self):
        return self.ct

    def calculate(self):
        bc = 0
        i = 0
        o = 0
        self.b = 2
        self.ct = [0] * self.n

        while True:
            while True:
                i = 0
                while i < self.n:
                    self.ct[i] += 1
                    o+=3
                    if self.ct[i] == (self.b - 1):
                        bc = bc + 1
                    if self.ct[i] < self.b:
                        break
                    self.ct[i] = 0
                    bc = bc - 1
                    i += 1
                if i < self.n:
                    break
                self.b += 1
            if bc > 0:
                actual_test = True
                for v in range(self.n):
                    if not actual_test:
                        break
                    neighbors = self.graph.get_neighbors(v)
                    for u in neighbors:
                        o += 1
                        if self.ct[v] == self.ct[u]:
                            actual_test = False
                            break
                if actual_test:
                    return o
