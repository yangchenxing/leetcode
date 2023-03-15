# @before-stub-for-debug-begin
# from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
from collections import deque

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        d = deque()
        d.append((height[0], 0))
        for i in range(1, len(height)):
            h2 = height[i]
            for h1, x in d:
                result = max(result, min(h1, h2) * (i - x))
            if h2 > d[-1][0]:
                d.append((h2, i))
        return result

# print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
# @lc code=end

