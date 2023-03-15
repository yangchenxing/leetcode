#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = ' ' + s
        s_len = len(s)
        dr = [False] * s_len
        dw = [False] * s_len
        dw[0] = True
        for token in self.tokenizer(p):
            dw, dr = dr, dw
            if token == '.':
                dw[0] = False
                for i in range(1, s_len):
                    dw[i] = dr[i - 1]
            elif len(token) == 1:
                dw[0] = False
                for i in range(1, s_len):
                    dw[i] = dr[i - 1] and s[i] == token
            elif token == '.*':
                dw[0] = dr[0]
                for i in range(1, s_len):
                    dw[i] = dr[i] or dw[i - 1]
            else:
                dw[0] = dr[0]
                for i in range(1, s_len):
                    dw[i] = (dr[i - 1] or dw[i - 1]) and s[i] == token[0] or dr[i]
        return dw[s_len - 1]
        
    def tokenizer(self, p):
        i = 0
        s = len(p)
        while i < s:
            if i + 1 < s and p[i + 1] == '*':
                yield p[i:i+2]
                i += 2
            else:
                yield p[i]
                i += 1               

# print(Solution().isMatch('aa', 'a'))
# print(Solution().isMatch('aa', 'a*'))
# print(Solution().isMatch('ab', '.*'))
# print(Solution().isMatch('mississippi', 'mis*is*ip*.'))
# print(Solution().isMatch('aab', 'c*a*b'))

# @lc code=end

