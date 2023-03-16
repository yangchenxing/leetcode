#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# from typing import *
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        tail = result
        p = ListNode(next=list1)
        q = ListNode(next=list2)
        while p.next and q.next:
            if p.next.val < q.next.val:
                tail.next = p.next
                p.next = p.next.next
            else:
                tail.next = q.next
                q.next = q.next.next
            tail = tail.next
            tail.next = None
        if p.next:
            tail.next = p.next
        elif q.next:
            tail.next = q.next
        return result.next

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
# print(to_list(Solution().mergeTwoLists(from_list([1,2,4]), from_list([1,3,4]))))
# print(to_list(Solution().mergeTwoLists(from_list([]), from_list([]))))
# print(to_list(Solution().mergeTwoLists(from_list([]), from_list([0]))))

# @lc code=end

