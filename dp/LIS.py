# 最长递增子序列(LIS), leetcode: 300
from sortedcontainers import *
def lengthOfLIS(nums: List[int]) -> int:
    sl = SortedList()
    for i, x in enumerate(nums):
        pos = sl.bisect_right((x, -i))
        if pos == len(sl): sl.add((x, -i))
        else:
            del sl[pos]
            sl.add((x, -i))
    return len(sl)