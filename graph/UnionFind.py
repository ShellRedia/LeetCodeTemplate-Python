from collections import *
'''
--- 从此处复制 ---
'''
class IdentityDefaultDict(defaultdict):
    '''
    该类用于处理并查集初始化的恒等映射
    '''
    def __missing__(self, key):
        return key

class UnionFind:
    def __init__(self, n=None):
        self.parent = IdentityDefaultDict()
        if n: self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def merge(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y: self.parent[x] = y
    def get_group_count(self):
        return len(set(self.find(x) for x in self.parent))