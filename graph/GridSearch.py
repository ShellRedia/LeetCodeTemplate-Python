from itertools import *
from collections import *
'''
--- 从此处复制 ---
'''
import numpy as np
class GridSearch:
    '''
    网格搜索(广度优先搜索):
    grid: 要进行搜索的矩阵，甚至立方 (二维数组或多维数组)
    mdist: 周围搜索限定范围，例如：abs(sum(pd)) == 1 为上下左右四格，abs(sum(pd)) <= 2 为周围八格
    '''
    def __init__(self, grid, mdist=1):
        grid = np.array(grid)
        s = set(product(*[range(x) for x in grid.shape]))
        dq = deque([(tuple(p), 0) for p in np.argwhere(grid == 1)])
        self.dist = np.full(grid.shape, np.inf)
        while dq:
            p, d = dq.popleft()
            for pd in product(*[range(-1, 2)] * len(grid.shape)):
                if abs(sum(pd)) == mdist:
                    t = tuple(map(sum, zip(p, pd)))
                    if t in s and self.dist[t] > d + 1:
                        self.dist[t] = d + 1
                        dq.append((t, d + 1))