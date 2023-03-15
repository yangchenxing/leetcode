#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start

M = [
    '',
    'M',
    'MM',
    'MMM'
]
C = [
    '',
    'C',
    'CC',
    'CCC',
    'CD',
    'D',
    'DC',
    'DCC',
    'DCCC',
    'CM'
]
X = [
    '',
    'X',
    'XX',
    'XXX',
    'XL',
    'L',
    'LX',
    'LXX',
    'LXXX',
    'XC'
]
I = [
    '',
    'I',
    'II',
    'III',
    'IV',
    'V',
    'VI',
    'VII',
    'VIII',
    'IX'
]


class Solution:
    def intToRoman(self, num: int) -> str:
        return ''.join(self.gen(num))

    def gen(self, num):
        if num >= 1000:
            yield M[num // 1000]
            num %= 1000
        if num >= 100:
            yield C[num // 100]
            num %= 100
        if num >= 10:
            yield X[num // 10]
            num %= 10
        if num:
            yield I[num]


# print(Solution().intToRoman(3))
# print(Solution().intToRoman(4))
# print(Solution().intToRoman(9))
# print(Solution().intToRoman(58))
# print(Solution().intToRoman(1994))

# @lc code=end
