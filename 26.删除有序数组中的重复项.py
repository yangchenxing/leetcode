#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
# from typing import *
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = None
        j = 0
        for num in nums:
            if num != last:
                last = nums[j] = num
                j += 1
        return j

# s = Solution()
# print(s.removeDuplicates([1,1,2]))
# print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
# @lc code=end

