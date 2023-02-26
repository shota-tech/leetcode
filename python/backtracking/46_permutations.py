# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        if len(nums) == 1:
            return [nums]

        for i in range(len(nums)):
            perms = self.permute(nums[:i] + nums[i + 1:])
            for perm in perms:
                res.append([nums[i]] + perm)

        return res
