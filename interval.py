# 区间问题，对于区间问题总有些共性可以总结:
# 并集
def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals: return []
    intervals.sort()
    merged = [intervals[0]]
    for x, y in intervals[1:]:
        if merged[-1][1] < x:
            merged.append([x, y])
        else:
            merged[-1][1] = max(y, merged[-1][1])
    return merged

# 交集
def intersection(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals: return []
    intervals.sort()
    intersection = []
    px, py = intervals[0]
    for x, y in intervals[1:]:
        if py >= x:
            intersection.append([max(px, x), min(py, y)])
        if y > py:
            px, py = x, y
    return intersection

