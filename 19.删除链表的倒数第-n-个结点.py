#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# from typing import *
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0:
            return head
        h = ListNode(next=head)
        p = h
        for i in range(n):
            p = p.next
        q = h
        while p.next:
            p = p.next
            q = q.next
        q.next = q.next.next
        return h.next


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
# print(to_list(Solution().removeNthFromEnd(from_list([1,2,3,4,5]), 2)))
# print(to_list(Solution().removeNthFromEnd(from_list([1,2]), 1)))        
# print(to_list(Solution().removeNthFromEnd(from_list([1]), 1)))        
# print(to_list(Solution().removeNthFromEnd(from_list([]), 0)))        

# @lc code=end

