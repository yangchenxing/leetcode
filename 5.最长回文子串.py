# @before-stub-for-debug-begin
# from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        best_i = 0
        best_j = 0
        m = len(s)
        # odd len
        for i in range(1, m - 1):
            i, j = i - 1, i + 1
            if s[i] != s[j]:  # fast check
                continue
            while i >= 0 and j < m and s[j] == s[i]:
                i, j = i - 1, j + 1
            if j - i - 2 > best_j - best_i:
                best_i, best_j = i + 1, j - 1
        # even len
        for i in range(0, m - 1):
            j = i + 1
            if s[i] != s[j]:  # fast check
                continue
            while i >= 0 and j < m and s[j] == s[i]:
                i, j = i - 1, j + 1
            if j - i - 2 > best_j - best_i:
                best_i, best_j = i + 1, j - 1
        return s[best_i:best_j+1]
            
# print(Solution().longestPalindrome("babad"))
# print(Solution().longestPalindrome("bb"))
# print(Solution().longestPalindrome("a"))

# @lc code=end

