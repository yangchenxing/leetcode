#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
# from typing import *

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        end = len(nums) - 1
        for i in range(end - 1, -1, -1):
            num = nums[i]
            if num >= nums[end]:
                for j in range(i, end):
                    nums[j] = nums[j + 1]
                nums[end] = num
            else:
                for j in range(i + 1, len(nums)):
                    if nums[j] > num:
                        nums[i] = nums[j]
                        nums[j] = num
                        break
                break

# s = Solution()
# nums = [1, 2, 3]
# s.nextPermutation(nums)
# print(nums)

# nums = [3, 2, 1]
# s.nextPermutation(nums)
# print(nums)

# nums = [1, 1, 5]
# s.nextPermutation(nums)
# print(nums)

# nums = [1, 5, 1]
# s.nextPermutation(nums)
# print(nums)


# @lc code=end

