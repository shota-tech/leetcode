# https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_to_copy = {None: None}
        current = head
        while current:
            original_to_copy[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            copy = original_to_copy[current]
            copy.next = original_to_copy[current.next]
            copy.random = original_to_copy[current.random]
            current = current.next

        return original_to_copy[head]
