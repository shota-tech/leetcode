# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digit_to_chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = []

        def backtrack(i: int, current: str):
            if i >= len(digits):
                res.append(current)
                return

            for c in digit_to_chars[digits[i]]:
                backtrack(i + 1, current + c)

        if digits:
            backtrack(0, "")

        return res
