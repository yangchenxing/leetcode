#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# from typing import *
from heapq import heapify, heappush, heappop


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class PriorityListNode:
    def __init__(self, node) -> None:
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [head for head in lists if head]
        lists = [PriorityListNode(head) for head in lists]
        heapify(lists)
        result = ListNode()
        tail = result
        while lists:
            priority_node = heappop(lists)
            tail.next = priority_node.node
            priority_node.node = priority_node.node.next
            tail = tail.next
            tail.next = None
            if priority_node.node is not None:
                heappush(lists, priority_node)
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
# s = Solution()
# print(to_list(s.mergeKLists([from_list([1,4,5]), from_list([1,3,4]), from_list([2,6])])))
# print(to_list(s.mergeKLists([from_list([1,4,5]), from_list([1,3,4]), from_list([])])))
# print(to_list(s.mergeKLists([])))
# @lc code=end
