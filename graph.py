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
