from collections import *
from bisect import *

'''
这个要题目明确说了是树才行，预处理出一些重要关系
'''


class TreeDoubling:
    '''
    parents: 父节点关系的数组，parents[i] 是 i 的父节点
    k: 最大查询范围，可以很大（10**10）,反正会指数折叠
    '''

    def __init__(self, parents, k):
        self.m = k.bit_length()
        pa = {}
        for x, p in parents.items():
            pa[x] = [p] + [None] * self.m
        for i in range(self.m):
            for x in parents:
                if pa[x][i]: pa[x][i + 1] = pa[pa[x][i]][i]
        self.pa = pa

    '''
    node: 要查询的节点
    k: 与节点x的距离
    '''

    def get_Kth_ancestor(self, node, k):
        for i in range(k.bit_length()):
            if (k >> i) & 1:
                node = self.pa[node][i]
                if node == None: return None
        return node


class GeneralTree:
    def __init__(self, n, edges):
        g = defaultdict(list)
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, w))
        parents, depth = {}, {}
        parents[0] = None
        dq = deque([(0, 0)])
        while dq:
            x, d = dq.popleft()
            depth[x] = d
            for y, w in g[x]:
                if y not in parents:
                    parents[y] = x
                    dq.append((y, d + 1))
        self.parents, self.depth = parents, depth
        self.td = TreeDoubling(parents, n)

    def get_node_parent(self, x):
        return self.parents[x]

    def get_node_depth(self, x):
        return self.depth[x]

    def get_lca(self, nodes):
        if not nodes: return -1
        depths = [self.get_node_depth(x) for x in nodes]
        mn_depth = min(depths)
        nodes = [self.td.get_Kth_ancestor(x, d - mn_depth) for x, d in zip(nodes, depths)]
        def check(lmt):
            return len(set(self.td.get_Kth_ancestor(x, lmt) for x in nodes)) == 1
        k = bisect_left(range(mn_depth), True, key=check)
        return self.td.get_Kth_ancestor(nodes[0], k)