#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
# from typing import *
from collections import deque

class Solution:
    letters = [
        None,
        None,
        'abc',
        'def',
        'ghi',
        'jkl',
        'mno',
        'pqrs',
        'tuv',
        'wxyz'
    ]

    def __init__(self):
        self.buffer = None
        self.result = None

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digits = [int(d) for d in digits]
        self.buffer = [None] * len(digits)
        self.result = deque()
        self.gen(digits, 0)
        return list(self.result)

    def gen(self, digits, p):
        for ch in Solution.letters[digits[p]]:
            self.buffer[p] = ch
            if p < len(digits) - 1:
                self.gen(digits, p + 1)
            else:
                self.result.append(''.join(self.buffer))


# print(Solution().letterCombinations('23'))
# print(Solution().letterCombinations('2'))
# print(Solution().letterCombinations('2345'))

# @lc code=end

