# 拓扑排序, 入参 n: 节点数量，contrains -> c, pc : 一个列表，表示节点和其前置节点
from graphlib import *
def topo_sort(n, constrains):
    '''
    :param n: 共 n 个点
    :param constrains: (c, pc)-> pc 是 c 的父亲节点
    :return: 拓扑排序的顺序列表，若为空，则不存在合法的拓扑排序
    '''
    ts = TopologicalSorter({c:{} for c in range(n)})
    for c, pc in constrains:ts.add(c, pc)
    if ts._find_cycle():return []
    return list(ts.static_order())