#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# from typing import *
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        temp = ListNode(next = head)
        a = temp
        b = head
        c = b.next
        while a and b and c:
            b.next = c.next
            a.next = c
            c.next = b
            a = a.next.next
            b = a.next if a else None
            c = b.next if b else None
        return temp.next

# def to_list(n):
#     res = []
#     while n:
#         res.append(n.val)
#         n = n.next
#     return res
# def from_list(nums):
#     h = ListNode()
#     t = h
#     for n in nums:
#         t.next = ListNode(n)
#         t = t.next
#     return h.next
# s = Solution()
# print(to_list(s.swapPairs(from_list([1,2,3,4]))))
# print(to_list(s.swapPairs(from_list([1,2,3,4,5]))))
# print(to_list(s.swapPairs(from_list([1,2]))))
# print(to_list(s.swapPairs(from_list([1]))))
# print(to_list(s.swapPairs(from_list([]))))
# H i j k
# a b c
# @lc code=end

