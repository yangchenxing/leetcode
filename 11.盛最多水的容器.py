# @before-stub-for-debug-begin
# from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = [None] * 10001
        right = [None] * 10001
        h_max = height[0]
        h_min = height[0]
        for i, h in enumerate(height):
            if left[h] is None:
                left[h] = right[h] = i
            else:
                right[h] = i
            h_min = min(h_min, h)
            h_max = max(h_max, h)
        most_left = left[h_max]
        most_right = right[h_max]
        result = 0
        for i in range(h_max, h_min - 1, -1):
            if left[i] is None:
                continue
            most_left = min(left[i], most_left)
            most_right = max(right[i], most_right)
            result = max(i * (most_right - most_left), result)
        return result

# print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
# @lc code=end

