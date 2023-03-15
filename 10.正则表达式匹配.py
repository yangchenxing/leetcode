#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p[0] != '*':
            mlen = self.match(s, 0, p, 0)
            return mlen and self.search(s, mlen, p, mlen)
        else:
            return bool(self.search(s, 0, p, 0))
        
    def search(self, s: str, sp: int, p: str, pp: int) -> bool:
        plen = len(p)
        for pp in range(pp, plen + 1):
            if pp == plen or p[pp] != '*':
                break
        if pp == len(p):
            return True
        for i in range(sp, len(s)):
            mlen = self.match(s, i, p, pp)
            if mlen:
                return self.search(s, sp + mlen, p, pp + mlen)
        return False

    def match(self, s, sp, p, pp):
        j = pp
        slen = len(s)
        plen = len(p)
        for i in range(sp, slen):
            if j >= plen:
                return False
            if p[j] == '*':
                return i - sp
            if p[j] != '.' and p[j] != s[i]:
                return False
            j += 1
        if j < plen and p[j] != '*':
            return False
        return slen - sp
                

# print(Solution().isMatch('aa', 'a'))
# print(Solution().isMatch('aa', 'a*'))
# print(Solution().isMatch('ab', '.*'))
# print(Solution().isMatch('abcba', 'a.*ab*'))
print(Solution().isMatch('aab', 'c*a*b'))

# @lc code=end

