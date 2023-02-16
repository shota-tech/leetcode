# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        m = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c not in m:
                stack.append(c)
                continue

            if not stack or stack[-1] != m[c]:
                return False

            stack.pop()

        return not stack
