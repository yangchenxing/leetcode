#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
from collections import deque

class Solution:
    lefts = ('(', '[', '{')
    right_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        stack = deque()
        for ch in s:
            if ch in Solution.lefts:
                stack.append(ch)
            elif not stack:
                return False
            else:
                pair = stack.pop()
                if pair != Solution.right_map[ch]:
                    return False
        return not stack


# print(Solution().isValid('()'))
# print(Solution().isValid('()[]{}'))
# print(Solution().isValid('(]'))
# @lc code=end

