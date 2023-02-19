# https://leetcode.com/problems/reorder-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list2 = slow.next
        slow.next = None
        prev = None
        while list2:
            nxt = list2.next
            list2.next = prev
            prev = list2
            list2 = nxt

        list1 = head
        list2 = prev
        while list2:
            nxt1 = list1.next
            nxt2 = list2.next
            list1.next = list2
            list2.next = nxt1
            list1 = nxt1
            list2 = nxt2
