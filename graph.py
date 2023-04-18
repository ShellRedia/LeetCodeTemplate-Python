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
p = list(range(10 ** 5 + 1))

# 广度优先搜索:
m, n = len(grid), len(grid[0])
dq = deque()
vis = set()
while dq:
    x, y = dq[0]
    dq.popleft()
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        cond = (grid[nx][ny] == 1) # 一些可能的其他条件，可替换
        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in vis and cond:
            dq.append((nx, ny))
            vis.add((nx, ny))
