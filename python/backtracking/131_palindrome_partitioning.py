# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        def backtrack(i: int, current: list[str]):
            if i >= len(s):
                res.append(current)
                return

            for j in range(i, len(s)):
                substr = s[i:j + 1]
                if self.isPalindrome(substr):
                    backtrack(j + 1, current + [substr])

        backtrack(0, [])
        return res

    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
