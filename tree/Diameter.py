from collections import *
from math import *

# 树的带权最长路径（直径）
class TreeDiameter:
    def __init__(self, edges):
        self.g = defaultdict(list)
        d1, d2 = Counter(), Counter()
        for x, y, w in edges:
            self.g[x].append((y, w))
            self.g[y].append((x, w))
        self.diameter = -inf
        def dfs(x, p):
            for y, w in self.g[x]:
                if y != p:
                    dfs(y, x)
                    t = d1[y] + w
                    if t > d1[x]:
                        d2[x], d1[x] = d1[x], t
                    elif t > d2[x]: d2[x] = t
            self.diameter = max(self.diameter, d1[x] + d2[x])
        dfs(edges[0][0], -1)

    def get_diameter(self):
        return self.diameter