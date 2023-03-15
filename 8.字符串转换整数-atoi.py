#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        for i in range(len(s)):
            if s[i] != ' ':
                break
        neg = False
        if i < len(s):
            if s[i] == '-':
                neg = True
                i += 1
            elif s[i] == '+':
                i += 1
        result = 0
        if not neg:
            for i in range(i, len(s)):
                ch = s[i]
                if '0' <= ch <= '9':
                    if result > 214748364 or result == 214748364 and ch >= '7':
                        return 2147483647
                    result = result * 10 + ord(ch) - 48
                else:
                    break
        else:
            for i in range(i, len(s)):
                ch = s[i]
                if '0' <= ch <= '9':
                    if result < -214748364 or result == -214748364 and ch >= '8':
                        return -2147483648
                    result = result * 10 - (ord(ch) - 48)
                else:
                    break
        return result


# print(Solution().myAtoi('42'))
# print(Solution().myAtoi('    -42'))
# print(Solution().myAtoi('4193 with words'))
# print(Solution().myAtoi('999999999'))
# print(Solution().myAtoi('99999999999'))
# print(Solution().myAtoi('-999999999'))
# print(Solution().myAtoi('-99999999999'))


# @lc code=end

