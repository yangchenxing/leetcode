#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# from typing import *
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head
        temp = ListNode(next=head)
        size = self.list_len(head)
        count = size // k
        p = temp
        for i in range(count):
            p = self.reverse(p, k)
        return temp.next

    def reverse(self, head, k):
        p = head.next
        for i in range(k - 1):
            temp = p.next
            p.next = temp.next
            temp.next = head.next
            head.next = temp
        return p

    def list_len(self, p):
        i = 0
        while p:
            i += 1
            p = p.next
        return i
    
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
# print(to_list(s.reverseKGroup(from_list([1,2,3,4,5]), 2)))
# print(to_list(s.reverseKGroup(from_list([1,2,3,4,5]), 3)))
# print(to_list(s.reverseKGroup(from_list([1,2,3,4,5,6]), 3)))
# print(to_list(s.reverseKGroup(from_list([1,2,3,4,5,6]), 1)))
# print(to_list(s.reverseKGroup(from_list([]), 3)))

# @lc code=end

