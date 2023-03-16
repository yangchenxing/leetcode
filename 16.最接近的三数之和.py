#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
# from typing import *
from collections import defaultdict

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        n_counts = sorted(counts.items())
        sums2 = set()
        best_diff = None
        best = None
        for n, count in n_counts:
            if count == 1:
                # update best
                best, best_diff = self.select_best(target, n, sums2, best, best_diff)
                # update sums2
                self.update_sums2(n, sums2, n_counts)
            elif count == 2:
                # update sums2
                self.update_sums2(n, sums2, n_counts)
                # update best
                best, best_diff = self.select_best(target, n, sums2, best, best_diff)
                # update n + n
                sums2.add(n + n)
            else:  # count >= 3
                # update sums2
                self.update_sums2(n, sums2, n_counts, False)
                # update best
                best, best_diff = self.select_best(target, n, sums2, best, best_diff)
        return best

    def select_best(self, target, n, sums2, best, best_diff):
        for s2 in sums2:
            sum3 = s2 + n
            diff = abs(target - sum3)
            if best is None or best_diff > diff:
                best, best_diff = sum3, diff
        return best, best_diff

    def update_sums2(self, n, sums2, n_counts, once=True):
        for m, cnt in n_counts:
            if m == n:
                if once:
                    continue
                if cnt > 1:
                    sums2.add(n + n)
            elif m > n:
                continue
            else:
                sums2.add(m + n)


# print(Solution().threeSumClosest([-1,2,1,-4], 1))
# print(Solution().threeSumClosest([0,0,0], 1))
# print(Solution().threeSumClosest([833,736,953,-584,-448,207,128,-445,126,248,871,860,333,-899,463,488,-50,-331,903,575,265,162,-733,648,678,549,579,-172,-897,562,-503,-508,858,259,-347,-162,-505,-694,300,-40,-147,383,-221,-28,-699,36,-229,960,317,-585,879,406,2,409,-393,-934,67,71,-312,787,161,514,865,60,555,843,-725,-966,-352,862,821,803,-835,-635,476,-704,-78,393,212,767,-833,543,923,-993,274,-839,389,447,741,999,-87,599,-349,-515,-553,-14,-421,-294,-204,-713,497,168,337,-345,-948,145,625,901,34,-306,-546,-536,332,-467,-729,229,-170,-915,407,450,159,-385,163,-420,58,869,308,-494,367,-33,205,-823,-869,478,-238,-375,352,113,-741,-970,-990,802,-173,-977,464,-801,-408,-77,694,-58,-796,-599,-918,643,-651,-555,864,-274,534,211,-910,815,-102,24,-461,-146], -7111))

# @lc code=end

