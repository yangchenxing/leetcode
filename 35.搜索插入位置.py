#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
# from typing import *
from bisect import bisect_left

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)


# s = Solution()
# print(s.searchInsert([1,3,5,6], 5))
# print(s.searchInsert([1,3,5,6], 2))
# print(s.searchInsert([1,3,5,6], 7))
# @lc code=end

