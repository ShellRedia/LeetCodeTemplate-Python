# 无重复全排列:
def permuteUnique(nums):
    if not nums: return []
    res = []
    used = [0] * len(nums)
    def backtracking(nums, used, path):
        # 终止条件
        if len(path) == len(nums):
            res.append(path.copy())
            return
        for i in range(len(nums)):
            if not used[i]:
                if i>0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtracking(nums, used, path)
                path.pop()
                used[i] = 0
    # 记得给nums排序
    backtracking(sorted(nums),used,[])
    return res

# 二维差分:快速地把一个矩形范围内的数都 + x
m, n = len(grid), len(grid[0])
diff = [[0] * (m + 2) for _ in range(n + 2)]
for r1, r2, c1, c2, x in rects:
    # 将区域 r1<=r<=r2 && c1<=c<=c2 上的数都加上 x
    # 多 +1 是为了方便求后面用二维前缀和复原
    diff[r1 + 1][c1 + 1] += x
    diff[r1 + 1][c2 + 2] -= x
    diff[r2 + 2][c1 + 1] -= x
    diff[r2 + 2][c2 + 2] += x
# 根据差分矩阵复原 (二维前缀和)，得到矩阵的真实值:
for i in range(1, n + 1):
    for j in range(1, m + 1):
        diff[i][j] += diff[i][j - 1] + diff[i - 1][j] - diff[i - 1][j - 1]
mat = diff

# 离散化
def discretize_dict(nums):
    s = set(nums)
    dct = dict(zip(sorted(s), range(len(s))))
    return dct
dct = discretize_dict(nums)
disc_arr = [dct[x] for x in nums]

# 最长递增子序列(LIS)
from sortedcontainers import *
def lengthOfLIS(nums: List[int]) -> int:
    sl = SortedList()
    for i, x in enumerate(nums):
        pos = sl.bisect_right((x, -i))
        if pos == len(sl):
            sl.add((x, -i))
        else:
            del sl[pos]
            sl.add((x, -i))
    return len(sl)

# 循环码(返回二进制字符串列表，参数n为二进制长度):
def cyclic_code(n):
    if n < 0:
        return []
    codes = ['0', '1']
    for i in range(n - 1):
        codes = [code + '0' for code in codes] + [code + '1' for code in reversed(codes)]
    return codes
