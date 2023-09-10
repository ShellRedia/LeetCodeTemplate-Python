# 无重复全排列:
class PermuteUnique:
    def __init__(self, nums):
        nums.sort()
        self.perm, used, path = [], [False] * len(nums), []

        def backtracking():
            # 终止条件
            if len(path) == len(nums):
                self.perm.append(path.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]: continue
                    used[i] = True
                    path.append(nums[i])
                    backtracking()
                    path.pop()
                    used[i] = False
        backtracking()

    def get_permutation(self):
        return self.perm
