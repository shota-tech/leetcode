# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(i: int, current: list[int], total: int):
            if total == target:
                res.append(current.copy())
                return
            if i >= len(candidates) or total > target:
                return

            current.append(candidates[i])
            backtrack(i + 1, current, total + candidates[i])
            current.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, current, total)

        backtrack(0, [], 0)
        return res
