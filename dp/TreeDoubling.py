# 树上倍增
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
                if pa[x][i]: pa[x][i+1] = pa[pa[x][i]][i]
        self.pa = pa
    '''
    node: 要查询的节点
    k: 与节点x的距离
    '''
    def get_Kth_ancestor(self, node, k):
        for i in range(k.bit_length()):
            if (k >> i) & 1:
                node = self.pa[node][i]
                if node is None: return None
        return node