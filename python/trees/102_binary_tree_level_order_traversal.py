# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        q = deque()
        res = []
        if root:
            q.append(root)

        while q:
            nodes = []
            for _ in range(len(q)):
                node = q.popleft()
                nodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(nodes)

        return res
