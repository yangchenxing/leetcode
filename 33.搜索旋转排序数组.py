#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
# from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return Solution.find_with_pivot(nums, 0, len(nums), target)

    @staticmethod
    def find_with_pivot(nums, lo, hi, target):
        if hi - lo <= 16:
            return Solution.simple_find(nums, lo, hi, target)
        mid = (hi + lo) // 2
        num_mid = nums[mid]
        if num_mid == target:
            return mid
        elif num_mid < nums[lo]:
            # pivot on left
            if num_mid <= target <= nums[hi - 1]:
                return Solution.find_without_pivot(nums, mid, hi, target)
            else:
                return Solution.find_with_pivot(nums, lo, mid, target)
        else:
            # pivot on right
            if nums[lo] <= target <= num_mid:
                return Solution.find_without_pivot(nums, lo, mid, target)
            else:
                return Solution.find_with_pivot(nums, mid, hi, target)

    @staticmethod
    def find_without_pivot(nums, lo, hi, target):
        if hi - lo <= 8:
            return Solution.simple_find(nums, lo, hi, target)
        mid = (hi + lo) // 2
        num_mid = nums[mid]
        if target == num_mid:
            return mid
        if target < num_mid:
            return Solution.find_without_pivot(nums, lo, mid, target)
        else:
            return Solution.find_without_pivot(nums, mid, hi, target)

    @staticmethod
    def simple_find(nums, lo, hi, target):
        for i in range(lo, hi):
            if nums[i] == target:
                return i
        return -1


# s = Solution()
# print(s.search([113,114,115,116,117,118,123,124,127,129,130,133,134,142,143,147,148,149,150,151,152,154,155,158,159,160,161,164,165,166,174,175,177,178,179,180,181,183,185,187,190,192,193,194,196,199,200,201,203,205,206,207,208,209,210,215,216,218,220,221,223,224,228,230,231,235,236,242,245,247,250,251,257,259,261,262,263,264,265,269,271,273,277,279,280,281,282,283,285,286,288,290,293,295,296,297,0,2,4,8,9,10,11,12,15,17,20,21,22,23,24,27,29,33,35,36,37,39,43,45,48,49,52,54,55,60,64,67,68,72,73,75,76,79,85,87,88,91,94,97,99,100,101,102,103,104,105,107,108,110,112], 296))
# print(s.search([57,58,59,62,63,66,68,72,73,74,75,76,77,78,80,81,86,95,96,97,98,100,101,102,103,110,119,120,121,123,125,126,127,132,136,144,145,148,149,151,152,160,161,163,166,168,169,170,173,174,175,178,182,188,189,192,193,196,198,199,200,201,202,212,218,219,220,224,225,229,231,232,234,237,238,242,248,249,250,252,253,254,255,257,260,266,268,270,273,276,280,281,283,288,290,291,292,294,295,298,299,4,10,13,15,16,17,18,20,22,25,26,27,30,31,34,38,39,40,47,53,54], 30))
# print(s.search([266,267,268,269,271,278,282,292,293,298,6,9,15,19,21,26,33,35,37,38,39,46,49,54,65,71,74,77,79,82,83,88,92,93,94,97,104,108,114,115,117,122,123,127,128,129,134,137,141,142,144,147,150,154,160,163,166,169,172,173,177,180,183,184,188,198,203,208,210,214,218,220,223,224,233,236,241,243,253,256,257,262,263], 208))
# print(s.search([4,5,6,7,0,1,2], 0))
# print(s.search([4,5,6,7,0,1,2], 3))
# print(s.search([1], 0))
# print(s.search([1], 1))
# print(s.search([4,5,6,7,0,1,2], 5))
# @lc code=end

