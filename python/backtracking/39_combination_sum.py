# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(i: int, path: list[int], total: int):
            if total == target:
                res.append(path)
                return
            if i >= len(candidates) or total > target:
                return

            backtrack(i, path + [candidates[i]], total + candidates[i])
            backtrack(i + 1, path, total)

        backtrack(0, [], 0)
        return res
