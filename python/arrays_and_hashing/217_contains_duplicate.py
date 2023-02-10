# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        prev = set()
        for n in nums:
            if n in prev:
                return True
            prev.add(n)
        return False
