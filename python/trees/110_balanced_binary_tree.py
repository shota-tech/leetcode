# https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]) -> tuple[bool, int]:
            if not root:
                return True, 0

            left_balanced, left_height = dfs(root.left)
            right_balanced, right_height = dfs(root.right)
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            return balanced, 1 + max(left_height, right_height)

        return dfs(root)[0]
