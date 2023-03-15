#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
M = [0] * 255
M[ord('I')] = 1
M[ord('V')] = 5
M[ord('X')] = 10
M[ord('L')] = 50
M[ord('C')] = 100
M[ord('D')] = 500
M[ord('M')] = 1000


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        last = 1000
        for ch in s:
            v = M[ord(ch)]
            result += v - (last << 1) if v > last else v
            last = v
        return result


# print(Solution().romanToInt('MCMXCIV'))
# print(Solution().romanToInt('LVIII'))
# @lc code=end
