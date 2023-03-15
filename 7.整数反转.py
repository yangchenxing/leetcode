# from types import *
#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        neg = x < 0
        x = abs(x)

        result = x % 10
        x = x // 10
        while not result:
            result = x % 10
            x //= 10
        while x:
            result = result * 10 + x % 10
            x //= 10
        if neg:
            result = -result
        
        return result if result <= 2147483647 and result >= -2147483648 else 0


# print(Solution().reverse(123))
# print(Solution().reverse(-123))
# print(Solution().reverse(120))
# print(Solution().reverse(0))
# print(Solution().reverse(1534236469))
# print(Solution().reverse(1463847412))

# @lc code=end

