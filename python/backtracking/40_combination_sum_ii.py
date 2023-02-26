# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(i: int, path: list[int], total: int):
            if total == target:
                res.append(path)
                return
            if i >= len(candidates) or total > target:
                return

            backtrack(i + 1, path + [candidates[i]], total + candidates[i])

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, path, total)

        backtrack(0, [], 0)
        return res
