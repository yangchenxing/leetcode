#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        neg = False
        if dividend < 0:
            neg = not neg
            dividend = -dividend
        if divisor < 0:
            neg = not neg
            divisor = -divisor
        if dividend < divisor:
            return 0
        
        w1 = self.get_width(dividend)
        w2 = self.get_width(divisor)
        v = divisor << (w1 - w2)
        p = 1 << (w1 - w2)
        result = 0
        for i in range(w1 - w2 + 1):
            if dividend >= v:
                result |= p
                dividend -= v
            v >>= 1
            p >>= 1
        if neg:
            result = -result
        if result > 2147483647:
            result = 2147483647
        elif result < -2147483648:
            result = -2147483648
        return result
    
    def get_width(self, v):
        w = 1
        p = 1
        v = v ^ p & v
        while v:
            w += 1
            p <<= 1
            v = v ^ p & v
        return w


# s = Solution()
# print(s.divide(10, 3))
# print(s.divide(7, -3))
# print(s.divide(-1, 1))

# @lc code=end

