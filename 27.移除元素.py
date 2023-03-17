#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i] == val:
                break
        j = i
        for i in range(i, len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j
# @lc code=end

