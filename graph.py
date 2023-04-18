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
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)] + [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        nx, ny = x + dx, y + dy
        cond = (grid[nx][ny] == 1) # 一些可能的其他条件，可替换
        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in vis and cond:
            dq.append((nx, ny))
            vis.add((nx, ny))
            
# 深度优先搜索: TODO

# 最短路径 
# Dijkstra: -- 单源无负权 -- :
g = defaultdict(list)
        
for s, t, v in edges:
    g[s].append((t,v+1))
    # g[t].append((s,v+1)) # 无向图

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
        for y, cost in table[x]:
            if dist[x] + cost < dist[y]:
                dist[y] = dist[x] + cost
                ss.add((dist[y], y))
    return dist

src = 0            
dist = get_dist(src) # src 到各个点的距离，保存为数组形式
