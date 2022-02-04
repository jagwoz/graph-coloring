class algorithm:
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
        o = 0
        dt = [0] * self.n
        vt = [0] * self.n
        c = [False] * self.n
        self.b = 2
        self.ct = [0] * self.n

        for v in range(self.n):
            o += 2
            vt[v] = v
            dt[v] = self.graph.get_degree(v)
            d = dt[v]
            j = v
            while j > 0 and dt[j - 1] < d:
                dt[j] = dt[j - 1]
                vt[j] = vt[j - 1]
                j -= 1
            dt[j] = d
            vt[j] = v

        for i in range(0, self.n):
            self.ct[i] = -1
        self.ct[vt[0]] = 0

        for v in range(1, self.n):
            for i in range(0, self.n):
                o += 1
                c[i] = False
            v_neighbors = self.graph.get_neighbors(vt[v])
            for i in range(len(v_neighbors)):
                o += 2
                u = v_neighbors[i]
                if self.ct[u] > -1:
                    c[self.ct[u]] = True;
            i = 0
            while c[i]:
                i = i + 1
            self.ct[vt[v]] = i
            if i + 1 > self.b:
                self.b = i + 1
        return o