'''
最小费用最大流，洛谷 P3381
'''
from collections import *
from math import *

class Node:
    def __init__(self):
        self.val, self.v, self.next, self.w = 0, 0, 0, 0
    def __str__(self):
        return "{}, {}, {}, {}".format(self.val, self.v, self.next, self.w)

class Dinic:
    def __init__(self, src, dst, n=5010):
        self.nodes = [Node() for _ in range(2)]
        self.top = 1
        self.s, self.t = src, dst
        self.N = n
        self.head, self.vis, self.dist = [0] * self.N, [0] * self.N, [inf] * self.N
        self.cost, self.maxflow = 0, 0
    
    def _add_edge(self, u, v, val, w):
        self.nodes.append(Node())
        self.top += 1
        self.nodes[self.top].v = v
        self.nodes[self.top].w = w
        self.nodes[self.top].val = val
        self.nodes[self.top].next = self.head[u]
        self.head[u] = self.top
    
    def add_edge(self, u, v, val, w=0):
        self._add_edge(u , v, val, w)
        self._add_edge(v, u, 0, -w)
    
    def spfa(self)->bool:
        self.vis, self.dist = [0] * self.N, [inf] * self.N
        self.dist[self.s], self.vis[self.s] = 0, 1
        dq = deque([self.s])
        
        while dq:
            u = dq.popleft()
            self.vis[u] = 0
            i = self.head[u]
            while i:
                d = self.nodes[i].v
                if self.dist[u] + self.nodes[i].w < self.dist[d] and self.nodes[i].val:
                    self.dist[d] = self.dist[u] + self.nodes[i].w
                    if self.vis[d] == 0: 
                        dq.append(d)
                        self.vis[d] = 1
                i = self.nodes[i].next
        return self.dist[self.t] != inf
    
    def dfs(self, u, flow)->int:
        if u == self.t:
            self.vis[self.t] = 1
            self.maxflow += flow
            return flow
        used = 0
        self.vis[u] = 1
        i = self.head[u]
        while i:
            d = self.nodes[i].v
            if (self.vis[d] == 0 or d == self.t) and self.nodes[i].val != 0 and self.dist[d] == self.dist[u] + self.nodes[i].w:
                minflow = self.dfs(d, min(flow-used, self.nodes[i].val))
                if minflow != 0:
                    self.cost += self.nodes[i].w * minflow
                    self.nodes[i].val -= minflow
                    self.nodes[i^1].val += minflow
                    used += minflow
                if used == flow: break
            i = self.nodes[i].next
        return used

    def get_max_flow_min_cost(self):
        while self.spfa():
            self.vis[self.t] = 1
            while self.vis[self.t]:
                self.vis = [0] * self.N
                self.dfs(self.s, inf)
        return self.maxflow, self.cost

# if __name__ == '__main__':
#     n, m, s, t = map(int, input().split())
#     dinic = Dinic(s, t)
#     for i in range(m):
#         u, v, val, w = map(int, input().split())
#         dinic.add_edge(u , v, val, w) # val->流量，w->费用
#     ans, cost = dinic.get_max_flow_min_cost()
#     print(ans, cost)