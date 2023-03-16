#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
# from typing import *
from collections import deque

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()
        for a, num_a in self.iter_nums(nums, 0, len(nums) - 3, 1):
            for b, num_b in self.iter_nums(nums, a + 1, len(nums) - 2, 1):
                iter_c = iter(self.iter_nums(nums, b + 1, len(nums) - 1, 1, True))
                iter_d = iter(self.iter_nums(nums, len(nums) - 1, b + 1, -1, True))
                c, num_c = next(iter_c)
                d, num_d = next(iter_d)
                while c and d and c < d:
                    s = num_a + num_b + num_c + num_d
                    if s == target:
                        result.add((num_a, num_b, num_c, num_d))
                        c, num_c = next(iter_c)
                        d, num_d = next(iter_d)
                    elif s < target:
                        c, num_c = next(iter_c)
                    else:
                        d, num_d = next(iter_d)
        return list(result)

    def iter_nums(self, nums, start, bound, step, end_with_none=False):
        last = None
        for i in range(start, bound, step):
            if last is None or last != nums[i]:
                yield i, nums[i]
                last = nums[i]
        if end_with_none:
            yield None, None

# print(Solution().fourSum([1,0,-1,0,-2,2], 0))
# print(Solution().fourSum([2,2,2,2], 8))
# print(Solution().fourSum([2,2,2,2,2], 8))
                    
# @lc code=end

