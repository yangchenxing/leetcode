#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
# from typing import *
from collections import deque, defaultdict

class Solution:
    bounded_result_buffers = defaultdict(deque)
    bounded_result_buffers[1] = ['()']
    bounded_result_buffers[2] = ['(())']
    full_result_buffers = defaultdict(deque)
    full_result_buffers[1] = ['()']
    full_result_buffers[2] = ['(())', '()()']
    def generateParenthesis(self, n: int) -> List[str]:
        return list(self.get_full_result(n))

    def get_full_result(self, n):
        result = Solution.full_result_buffers[n]
        if result:
            return result
        buffer = deque()
        self.gen_full_result(result, buffer, n)
        return result

    def gen_full_result(self, result, buffer, n):
        for i in range(1, n+1):
            for r in self.get_bounded_result(i):
                buffer.append(r)
                if i == n:
                    result.append(''.join(buffer))
                else:
                    self.gen_full_result(result, buffer, n - i)
                buffer.pop()

    def get_bounded_result(self, n):
        result = Solution.bounded_result_buffers[n]
        if result:
            return result
        buffer = deque()
        buffer.append('(')
        for r in self.get_full_result(n - 1):
            buffer.append(r)
            buffer.append(')')
            result.append(''.join(buffer))
            buffer.pop()
            buffer.pop()
        return result

# s = Solution()
# print(s.generateParenthesis(3))
# print(s.generateParenthesis(1))
# print(s.generateParenthesis(4))
# @lc code=end

