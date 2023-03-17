#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
# from typing import *
from bisect import bisect_left

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = Solution.find_pivot(nums, 0, len(nums))
        if nums[0] <= target <= nums[pivot]:
            pos = bisect_left(nums, target, 0, pivot + 1)
        elif pivot < len(nums) - 1 and nums[pivot + 1] <= target <= nums[len(nums) - 1]:
            pos = bisect_left(nums, target, pivot + 1)
        else:
            return -1
        return pos if nums[pos] == target else -1

    @staticmethod
    def find_pivot(nums, lo, hi):
        if hi - lo <= 8:
            for i in range(lo, hi - 1):
                if nums[i] > nums[i + 1]:
                    return i
            return hi - 1
        mid = (hi + lo) // 2
        if nums[mid] < nums[lo]:
            return Solution.find_pivot(nums, lo, mid)
        else:
            return Solution.find_pivot(nums, mid, hi)


# s = Solution()
# print(s.search([4,5,6,7,0,1,2], 0))
# print(s.search([4,5,6,7,0,1,2], 3))
# print(s.search([1], 0))
# print(s.search([1], 1))
# print(s.search([4,5,6,7,0,1,2], 5))
# @lc code=end

