# 区间问题 范围 [L, R), 新增区间后合并已有区间

from math import *
from sortedcontainers import *

'''
这个是一边添加一边合并已有区间的板子，不能反悔
'''
class Interval:
    def __init__(self):
        self.sl = SortedList([(-inf, -inf), (inf, inf)])

    def add(self, start, end) -> None:
        x, y = start, end
        p = self.sl.bisect_left((start, end))
        while self.sl[p][0] <= end:
            x, y = min(x, self.sl[p][0]), max(y, self.sl[p][1])
            self.sl.pop(p)
            p = self.sl.bisect_left((start, end))
        while start <= self.sl[p-1][1]:
            x, y = min(x, self.sl[p-1][0]), max(y, self.sl[p-1][1])
            self.sl.pop(p-1)
            p = self.sl.bisect_left((start, end))
        self.sl.add((x, y))

    def is_intersect(self, start, end) -> bool:
        p = self.sl.bisect_left((start, end))
        return self.sl[p][0] < end or start < self.sl[p-1][1]

    def get_intersections(self, start, end) -> list:
        p = self.sl.bisect_left((start, end))
        l, r = p-1, p
        rnt = []
        while r < len(self.sl) and self.sl[r][0] < end:
            rnt.append((max(start, self.sl[r][0]), min(end, self.sl[r][1])))
            r += 1
        while l >= 0 and start < self.sl[l][1]:
            rnt.append((max(start, self.sl[l][0]), min(end, self.sl[l][1])))
            l -= 1
        return rnt

    def get_intervals(self) -> list:
        return list(self.sl)[1:-1]
