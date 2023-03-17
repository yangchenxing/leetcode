#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
# from typing import *

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return (-1, -1)
        lo = 0
        hi = len(nums)
        fake_target = target - 0.5
        while hi - lo > 16:
            mid = (lo + hi) // 2
            if fake_target < nums[mid]:
                hi = mid
            else:
                lo = mid
        end = len(nums) - 1
        hi = min(len(nums), hi + 1)
        while lo < hi - 1 and nums[lo] < target:
            lo += 1
        if nums[lo] != target:
            return (-1, -1)
        hi = lo
        while hi < end and nums[hi + 1] == target:
            hi += 1
        return lo, hi

# s = Solution()
# print(s.searchRange([2,2], 3))
# print(s.searchRange([1], 1))
# print(s.searchRange([5,7,7,8,8,10], 8))
# print(s.searchRange([5,7,7,8,8,10], 6))
# print(s.searchRange([], 0))
# @lc code=end

