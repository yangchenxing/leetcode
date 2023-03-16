#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
from heapq import heapify, heappush, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class PriorityListNode:
    def __init__(self, node) -> None:
        self.node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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
        # @lc code=end
