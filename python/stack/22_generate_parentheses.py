# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(open_n: int, close_n: int):
            if open_n == close_n == n:
                res.append(''.join(stack))
                return

            if open_n < n:
                stack.append('(')
                backtrack(open_n + 1, close_n)
                stack.pop()

            if close_n < open_n:
                stack.append(')')
                backtrack(open_n, close_n + 1)
                stack.pop()

        backtrack(0, 0)
        return res