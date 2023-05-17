# 并查集
def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def merge(a, b):
    x, y = find(a), find(b)
    if x == y:
        return
    p[x] = y
N = 10 ** 5 + 1
p = list(range(N))

# 广度优先搜索:
m, n = len(grid), len(grid[0])
dq = deque()
vis = set()
while dq:
    x, y = dq[0]
    dq.popleft()
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # + [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in vis:
            if grid[nx][ny] == 1: # 一些可能的其他条件，可替换
                dq.append((nx, ny))
                vis.add((nx, ny))
            
# 深度优先搜索: TODO

# 最短路径 
# Dijkstra: -- 单源无负权 -> 适合于修改少，查询多的情况: 
# 开头需要import平衡树: from sortedcontainers import *

g = defaultdict(list)
        
for x, y, w in edges:
    g[x].append((y, w))
    # g[y].append((x, w)) # 无向图

def get_dist(src):
    dist=[inf]*n
    dist[src]=0   
    ss = SortedSet()

    ss.add((0, src))
    while ss:
        d, x = ss[0]
        ss.remove((d,x))
        if d > dist[x] or dist[x] == inf:
            continue
        for y, cost in g[x]:
            if dist[x] + cost < dist[y]:
                dist[y] = dist[x] + cost
                ss.add((dist[y], y))
    return dist

src = 0            
dist = get_dist(src) # src 到各个点的距离，保存为数组形式

# Floyd 单源无负权 -> 适合于点数少，修改多的情况:
# 建图
d = [[inf] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for x, y, w in edges:
    d[x][y] = w  # 添加一条边（输入保证没有重边和自环）
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
# 加边
x, y, w = edge
if w >= d[x][y]:  # 无需更新
    return
for i in range(n):
    for j in range(n):
        d[i][j] = min(d[i][j], d[i][x] + w + d[y][j])
# 求最短路
src, tgt = 0, 1
dist = d[src][tgt]

# 拓扑排序, 入参 n: 节点数量，contrains -> c, pc : 一个列表，表示节点和其前置节点 
from graphlib import *
def topo_sort(n, constrains):
    ts = TopologicalSorter({c:{} for c in range(n)})
    for c, pc in constrains:
        ts.add(c, pc)
    if ts._find_cycle():
        return []
    return list(ts.static_order())
