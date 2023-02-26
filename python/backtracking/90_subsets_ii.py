# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        def backtrack(i: int, path: list[int]):
            if i >= len(nums):
                res.append(path)
                return

            backtrack(i + 1, path + [nums[i]])

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, path)

        backtrack(0, [])
        return res
