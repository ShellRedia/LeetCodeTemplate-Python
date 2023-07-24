from collections import *
from itertools import *
# 并查集
import numpy as np
class UnionFind:
    def __init__(self):
        self.parent = defaultdict(lambda:None)
    def find(self, x):
        if self.parent[x] != x: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def merge(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y: self.parent[x] = y
    def count_groups(self):
        return len(set(self.find(x) for x in self.parent))


# 网格搜索(广度优先搜索):
import numpy as np
class GridSearch:
    def __init__(self, grid, mdist=1):
        grid = np.array(grid)
        s = set(product(*[range(x) for x in grid.shape]))
        dq = deque([(tuple(p), 0) for p in np.argwhere(grid == 1)])
        self.dist = np.full(grid.shape, np.inf)
        while dq:
            p, d = dq.popleft()
            for pd in product(*[range(-1, 2)] * len(grid.shape)):
                if abs(sum(pd)) == mdist:
                    t = tuple(map(lambda x: sum(x), zip(p, pd)))
                    if t in s and self.dist[t] > d + 1:
                        self.dist[t] = d + 1
                        dq.append((t, d + 1))



# 深度优先搜索: TODO

# 最短路径 
# Dijkstra: -- 单源无负权 -> 适合于修改少，查询多的情况:
from sortedcontainers import *
class Dijkstra:
    def __init__(self, edges, undirected=True):
        self.g = defaultdict(list)
        for x, y, w in edges:
            self.g[x].append((y, w))
            if undirected: self.g[y].append((x, w))
    def get_dist(self, src=0):
        dist = defaultdict(lambda : inf)
        dist[src] = 0
        ss = SortedSet([(dist[src], src)])
        while ss:
            d, x = ss.pop(0)
            for y, cost in self.g[x]:
                if dist[x] + cost < dist[y]:
                    dist[y] = dist[x] + cost
                    ss.add((dist[y], y))
        return dist


# Floyd 单源无负权 -> 适合于点数少，修改多的情况:
# 建图
class Floyd:
    def __init__(self, edges, undirected=True):
        self.d = d = defaultdict(lambda:inf)
        self.undirected = undirected
        self.nodes = set()
        for x, y, w in edges:
            self.nodes.add(x)
            self.nodes.add(y)
            d[(x, x)] = d[(y, y)] = 0
            d[(x, y)] = w
            if undirected: d[(y, x)] = w
        for k, i, j in product(*[self.nodes] * 3):
            d[(i, j)] = min(d[(i, j)], d[(i, k)] + d[(k, j)])
    def add_edge(self, edge): # 加边
        x, y, w = edge
        d = self.d
        self.nodes.add(x)
        self.nodes.add(y)
        d[(x, x)] = d[(y, y)] = 0
        if d[(x, y)] <= w: return
        for i, j in product(*[self.nodes] * 2):
            d[(i, j)] = min(d[(i, j)], d[(i, x)] + w + d[(y, j)])
            if self.undirected: d[(i, j)] = min(d[(i, j)], d[(i, y)] + w + d[(x, j)])
    def get_dist(self, x, y):
        d = self.d
        d[(x, x)] = d[(y, y)] = 0
        self.nodes.add(x)
        self.nodes.add(y)
        return d[(x, y)]

from sortedcontainers import *
class Hierholzer:
    def __init__(self, edges, undirected=True):
        self.g = defaultdict(SortedList)
        for x, y in edges:
            self.g[x].add(y)
            if undirected: self.g[y].add(x)
    def get_path(self, src=0):
        g = deepcopy(self.g)
        path = []
        def dfs(x):
            while g[x]: dfs(g[x].pop(0))
            path.append(x)
        dfs(src)
        return path[::-1]

# 拓扑排序, 入参 n: 节点数量，contrains -> c, pc : 一个列表，表示节点和其前置节点 
from graphlib import *
def topo_sort(n, constrains):
    ts = TopologicalSorter({c:{} for c in range(n)})
    for c, pc in constrains: ts.add(c, pc)
    if ts._find_cycle():return []
    return list(ts.static_order())

# tarjan 求桥与割点(无向图):
def tarjan(edges):
    root = edges[0][0]
    g, childrens = defaultdict(list), defaultdict(list)
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
                childrens[x].append(y)
            low[x] = min(low[x], low[y])
    f(root, -1)
    bridges = sorted([x, y] for x, y in edges2 if low[y] > dfn[x])
    artis = []  # 割点
    for x, ys in childrens.items():
        if x == root and len(childrens[x]) >= 2: artis.append(x)
        if x != root:
            for y in ys:
                if low[y] >= dfn[x]:
                    artis.append(x)
                    break
    return bridges, artis

# 树的直径(包括二叉树):
diameter, node_t = 0, None
def dfs(x, fa, d):
    nonlocal diameter, node_t
    if d > diameter: diameter, node_t = d, x
    for y in g[x]:
        if y != fa: dfs(y, x, d + 1)
dfs(root, None, 0)
dfs(node_t, None, 0)
diameter