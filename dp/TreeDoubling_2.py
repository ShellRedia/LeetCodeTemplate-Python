class TreeDoubling:
    '''
    parents: 父节点关系的数组，parents[i] 是 i 的父节点
    k: 最大查询范围，可以很大（10**10）,反正会指数折叠
    '''
    def __init__(self, parents, k):
        self.m = k.bit_length()
        pa = {}
        for x, p in parents.items():
            pa[x] = [(p, p)] + [(None, 0)] * self.m
        for i in range(self.m):
            for x in parents:
                p, s = pa[x][i]
                if p == None: break
                pp, ps = pa[p][i]
                pa[x][i+1] = (pp, ps + s) # ps + s 是累加关系，根据需要修改
        self.pa = pa
    '''
    node: 要查询的节点
    k: 与节点x的距离
    '''
    def get_Kth_ancestor(self, node, k):
        s0 = node
        for j in range(k.bit_length()):
            if (k >> j) & 1:
                node, s = self.pa[node][j]
                if node == None: return None, 0
                s0 += s # 与 ps + s 的累加关系对应修改
        return node, s0