#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return Solution.find_with_pivot(nums, 0, len(nums), target)

    @staticmethod
    def find_with_pivot(nums, lo, hi, target):
        if hi - lo <= 8:
            return Solution.simple_find(nums, lo, hi, target)
        num_lo = nums[lo]
        num_hi = nums[hi - 1]
        mid = (hi + lo) // 2
        num_mid = nums[mid]
        if num_mid < num_lo:
            # pivot on left
            if num_mid <= target <= num_hi:
                return Solution.find_without_pivot(nums, mid, hi, target)
            else:
                return Solution.find_with_pivot(nums, lo, mid, target)
        else:
            # pivot on right
            if num_lo <= target <= num_mid:
                return Solution.find_without_pivot(nums, lo, mid, target)
            else:
                return Solution.find_without_pivot(nums, mid, hi, target)

    @staticmethod
    def find_without_pivot(nums, lo, hi, target):
        num_lo = nums[lo]
        mid = (hi + lo) // 2
        num_mid = nums[mid]
        if num_mid < num_lo:
            return Solution.find_without_pivot(nums, lo, mid, target)
        else:
            return Solution.find_without_pivot(nums, mid, hi, target)

    @staticmethod
    def simple_find(nums, lo, hi, target):
        for i in range(lo, hi):
            if nums[i] == target:
                return i
        return -1



s = Solution()
print(s.search([266,267,268,269,271,278,282,292,293,298,6,9,15,19,21,26,33,35,37,38,39,46,49,54,65,71,74,77,79,82,83,88,92,93,94,97,104,108,114,115,117,122,123,127,128,129,134,137,141,142,144,147,150,154,160,163,166,169,172,173,177,180,183,184,188,198,203,208,210,214,218,220,223,224,233,236,241,243,253,256,257,262,263], 208))
# print(s.search([4,5,6,7,0,1,2], 0))
# print(s.search([4,5,6,7,0,1,2], 3))
# print(s.search([1], 0))
# print(s.search([1], 1))
# print(s.search([4,5,6,7,0,1,2], 5))
# @lc code=end

