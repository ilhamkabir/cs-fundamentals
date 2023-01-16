class Graph:
    def __init__(self, size):
        self.adj_list = [[] for i in range(size)]


    def add_edge(self, start, end, bi_dir=True):
        self.adj_list[start].append(end)
        if bi_dir:
            self.adj_list[end].append(start)
    
    def has_eulerian_cycle(self):
        odd = 0
        for vertex in self.adj_list:
            if len(self.adj_list[vertex]) % 2 == 1:
                odd += 1
        if odd == 0:
            return True
        return False

    def has_eulerian_path(self):
        odd = 0
        for vertex in self.adj_list:
            if len(self.adj_list[vertex]) % 2 == 1:
                odd += 1
        if odd == 0 or odd == 2:
            return True
        return False


graph = Graph(10)
graph.add_edge(0, 1)
graph.add_edge(0, 6)
graph.add_edge(0, 8)
graph.add_edge(1, 4)

print(graph.adj_list)