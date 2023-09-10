from itertools import *
'''
中位数贪心, 每次挑选一个元素加减1，求将数组中的数变为同一个数的最小代价
e.g.: LeetCode: 462. 最小操作次数使数组元素相等
'''
def MedianMove(nums):
    nums.sort()
    acc = [0] + list(accumulate(nums))
    n = len(nums)
    return acc[0] + acc[n] - 2 * acc[n//2] - nums[n//2] * (n & 1)