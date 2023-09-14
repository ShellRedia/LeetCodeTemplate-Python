'''
最大流
'''
from collections import *
from math import *
class FlowEdge:
    def __init__(self, x:int, y:int, cap:int):
        self.x, self.y, self.cap, self.flow = x, y, cap, 0
class Dinic:
    def __init__(self, n, edges, s=0, t=0):
        self.edges = []
        self.g = [[] for _ in range(n)]
        for x, y, w in edges: self.add_edge(x, y, w)
        self.dq = deque()
        self.level, self.ptr = [], []
        self.s, self.t, self.n = s, t, n

    def add_edge(self, x, y, cap) -> None:
        m = len(self.edges)
        self.edges.append(FlowEdge(x, y, cap))
        self.edges.append(FlowEdge(y, x, 0))
        self.g[x].append(m)
        self.g[y].append(m+1)

    def bfs(self) -> bool:
        while self.dq:
            x = self.dq.popleft()
            for id in self.g[x]:
                if self.edges[id].cap - self.edges[id].flow < 1: continue
                if self.level[self.edges[id].y] != -1: continue
                self.level[self.edges[id].y] = self.level[x] + 1
                self.dq.append(self.edges[id].y)
        return self.level[self.t] != -1

    def dfs(self, x, pushed) -> int:
        if not pushed: return 0
        if x == self.t: return pushed
        for cid in range(self.ptr[x], len(self.g[x])):
            id = self.g[x][cid]
            y = self.edges[id].y
            if self.level[x] + 1 != self.level[y] or self.edges[id].cap - self.edges[id].flow < 1: continue
            tr = self.dfs(y, min(pushed, self.edges[id].cap - self.edges[id].flow))
            if not tr: continue
            self.edges[id].flow += tr
            self.edges[id ^ 1].flow -= tr
            self.ptr[x] += 1
            return tr
        return 0

    def flow(self) -> int:
        rnt = 0
        while True:
            self.level = [-1] * self.n
            self.level[self.s] = 0
            self.dq.append(self.s)
            if not self.bfs(): break
            self.ptr = [0] * self.n
            pushed = self.dfs(self.s, inf)
            while pushed:
                rnt += pushed
                pushed = self.dfs(self.s, inf)
        return rnt

if __name__=="__main__":
    m, n = [int(x) for x in input().split()]
    edges = []
    for _ in range(m):
        x, y, w = [int(k) for k in input().split()]
        edges.append((x-1, y-1, w))
    dinic = Dinic(n, edges, 0, n-1)
    print(dinic.flow())