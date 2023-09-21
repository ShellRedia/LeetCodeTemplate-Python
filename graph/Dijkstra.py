from heapq import *
from collections import *
from math import *
'''
--- 从此处复制 ---
'''
class Dijkstra:
    '''
    最短路径：单源无负权 -> 适合于修改少，查询多的情况
    edges: 边: [[x1, y1], [x2, y2], ... ,[xn, yn]]
    undirected: 是否为有向图，默认无向图
    '''
    def __init__(self, edges=[], undirected=True):
        self.g = defaultdict(list)
        self.undirected = undirected
        for x, y, w in edges: self.add_edge(x, y, w)
    '''
    获取从 src 到其他点的距离，例如点0 到 点2 的距离: get_dist(0)[2]
    '''
    def get_min_dist(self, src=0):
        dist = defaultdict(lambda:inf)
        dist[src] = 0
        sl = [(dist[src], src)]
        while sl:
            d, x = heappop(sl)
            for y, cost in self.g[x]:
                if dist[x] + cost < dist[y]:
                    dist[y] = dist[x] + cost
                    heappush(sl, (dist[y], y))
        return dist
    
    def add_edge(self, x, y, w):
        self.g[x].append((y, w))
        if self.undirected: self.g[y].append((x, w))

# if __name__=='__main__':
#     edges = [[1,3,4], [3,4,5]]
#     dijkstra = Dijkstra(edges=edges, undirected=True) # 无向图
#     # dijkstra.add_edge(x, y, w)
#     src, dst = 0, 1
#     min_dist = dijkstra.get_min_dist(src=src)[dst]