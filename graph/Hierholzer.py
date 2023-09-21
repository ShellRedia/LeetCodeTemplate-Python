from collections import *
from heapq import *
from copy import deepcopy

# Hierholzer是一种解决欧拉回路问题的算法，该问题涉及在图中找到一个遍历所有边恰好一次，并且最终回到起始点的闭合路径。
class Hierholzer:
    def __init__(self, edges=[], undirected=True):
        self.g = defaultdict(list)
        self.undirected = undirected
        for x, y in edges: self.add_edge(x, y)

    def get_path(self, src=0):
        g = deepcopy(self.g)
        path = []
        def dfs(x):
            while g[x]: dfs(heappop(g[x]))
            path.append(x)
        dfs(src)
        return path[::-1]
    
    def add_edge(self, x, y):
        heappush(self.g[x], y)
        if self.undirected: heappush(self.g[y], x)

# hierholzer = Hierholzer(edges=edges, undirected=True)
# # hierholzer.add_edge(x, y)
# path = hierholzer.get_path(src=0)
