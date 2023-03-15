#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        return ''.join(self.gen(num))

    def gen(self, num):
        while num >= 1000:
            yield 'M'
            num -= 1000
        if num >= 900:
            yield 'CM'
            num -= 900
        if num >= 500:
            yield 'D'
            num -= 500
        if num >= 400:
            yield 'CD'
            num -= 400
        while num >= 100:
            yield 'C'
            num -= 100
        if num >= 90:
            yield 'XC'
            num -= 90
        if num >= 50:
            yield 'L'
            num -= 50
        if num >= 40:
            yield 'XL'
            num -= 40
        while num >= 10:
            yield 'X'
            num -= 10
        if num >= 9:
            yield 'IX'
            num -= 9
        if num >= 5:
            yield 'V'
            num -= 5
        if num >= 4:
            yield 'IV'
            num -= 4
        for i in range(num):
            yield 'I'


# print(Solution().intToRoman(3))
# print(Solution().intToRoman(4))
# print(Solution().intToRoman(9))
# print(Solution().intToRoman(58))
# print(Solution().intToRoman(1994))
        
# @lc code=end

