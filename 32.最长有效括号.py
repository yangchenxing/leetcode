#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start

# from types import *

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [None] * len(s)
        result = 0
        p = 0
        for ch in s:
            if ch == '(':
                # push
                stack[p] = ch
                p += 1
            else:
                count = 0
                matched = False
                while p:
                    top = stack[p - 1]
                    if top == '(':
                        if not matched:
                            count += 2
                            matched = True
                            p -= 1
                        else:
                            break
                    else:
                        count += top
                        p -= 1
                if matched:
                    if count > result:
                        result = count
                    stack[p] = count
                    p += 1
                else:
                    p = 0
        return result


# print(Solution().longestValidParentheses('(()'))
# print(Solution().longestValidParentheses(')()())'))
# print(Solution().longestValidParentheses(''))
                
# @lc code=end

