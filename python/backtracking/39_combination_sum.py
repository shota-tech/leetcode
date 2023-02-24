# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(i: int, current: list[int], total: int):
            if total == target:
                res.append(current.copy())
                return
            if i >= len(candidates) or total > target:
                return

            current.append(candidates[i])
            backtrack(i, current, total + candidates[i])
            current.pop()
            backtrack(i + 1, current, total)

        backtrack(0, [], 0)
        return res
