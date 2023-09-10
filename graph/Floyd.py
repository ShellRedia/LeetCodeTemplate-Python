from itertools import *
from collections import *
from math import *
'''
--- 从此处复制 ---
'''
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