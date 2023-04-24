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

# 循环码(返回二进制字符串列表，参数n为二进制长度):
def cyclic_code(n):
    if n < 0:
        return []
    codes = ['0', '1']
    for i in range(n - 1):
        codes = [code + '0' for code in codes] + [code + '1' for code in reversed(codes)]
    return codes
