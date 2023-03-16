#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
# from typing import *
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        nums = sorted(counts.keys())
        
        result = []
        
        for i, ni in enumerate(nums):
            cnt = counts[ni]
            if ni == 0:
                if cnt >= 3:
                    result.append((0, 0, 0))
                continue
            if cnt >= 2 and -ni * 2 in counts:
                result.append((ni, ni, -ni * 2))
            for j in range(i + 1, len(nums)):
                nj = nums[j]
                nk = -ni - nj
                if nk <= nj:
                    break
                if nk in counts:
                    result.append((ni, nj, nk))
        return result

# print(Solution().threeSum([-1,0,1,2,-1,-4]))
# print(Solution().threeSum([0,1,1]))
# print(Solution().threeSum([0,0,0]))
# print(Solution().threeSum([-2,0,0,2,2]))
# @lc code=end

