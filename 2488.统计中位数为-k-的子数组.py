#
# @lc app=leetcode.cn id=2488 lang=python3
#
# [2488] 统计中位数为 K 的子数组
#

# @lc code=start
# from typing import *
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        kp = nums.index(k)
        lefts = defaultdict(int)
        lefts[0] += 1
        less = 0
        for i in range(kp - 1, -1, -1):
            less += 1 if nums[i] < k else -1
            lefts[less] += 1
        rights = defaultdict(int)
        rights[0] += 1
        greater = 0
        for i in range(kp + 1, len(nums)):
            greater += 1 if nums[i] > k else -1
            rights[greater] += 1
        result = 0
        for less, less_count in lefts.items():
            result += less_count * rights.get(less, 0) + less_count * rights.get(less + 1, 0)
        return result

# print(Solution().countSubarrays([3,2,1,4,5], 4))
# print(Solution().countSubarrays([2,3,1], 3))
# @lc code=end

