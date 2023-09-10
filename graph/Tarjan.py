from collections import *
from math import *
# tarjan 求桥与割点(无向图):
class Tarjan:
    def __init__(self, edges):
        root = edges[0][0]
        g, children = defaultdict(list), defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        dfn, low = defaultdict(lambda: inf), defaultdict(lambda: inf)
        edges2, ts = [], 0  # edges2: 除去子节点到父节点边的集合

        def f(x, p):
            nonlocal ts
            low[x] = dfn[x] = ts = ts + 1
            for y in g[x]:
                if y == p: continue
                edges2.append([x, y])
                if dfn[y] == inf:
                    f(y, x)
                    children[x].append(y)
                low[x] = min(low[x], low[y])
        f(root, -1)
        bridges = sorted([x, y] for x, y in edges2 if low[y] > dfn[x])
        artis = []  # 割点
        for x, ys in children.items():
            if x == root and len(children[x]) >= 2: artis.append(x)
            if x != root:
                for y in ys:
                    if low[y] >= dfn[x]:
                        artis.append(x)
                        break
        self.bridges, self.artis = bridges, artis

    # 获取所有桥: 例题: leetcode: 1192. 查找集群内的关键连接
    def get_bridges(self):
        return self.bridges

    # 获取所有割点
    def get_artis(self):
        return self.artis
