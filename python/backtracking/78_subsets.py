# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(i: int, path: list[int]):
            if i == len(nums):
                res.append(path)
                return

            backtrack(i + 1, path + [nums[i]])
            backtrack(i + 1, path)

        backtrack(0, [])
        return res
