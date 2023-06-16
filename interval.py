# 区间问题，对于区间问题总有些共性可以总结:
# 合并
def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals: return []
    intervals.sort()
    merged_intervals = [intervals[0]]
    for x, y in intervals[1:]:
        if merged_intervals[-1][1] < x:
            merged_intervals.append([x, y])
        else:
            merged_intervals[-1][1] = max(y, merged_intervals[-1][1])
    return merged_intervals

# 求交集
def intersection(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    ans = []
    i = j = 0
    while i < len(A) and j < len(B):
        lo = max(A[i][0], B[j][0])
        hi = min(A[i][1], B[j][1])
        if lo <= hi:
            ans.append([lo, hi])
        if A[i][1] < B[j][1]: i += 1
        else: j += 1
    return ans

