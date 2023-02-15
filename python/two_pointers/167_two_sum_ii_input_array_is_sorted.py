# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            current = numbers[l] + numbers[r]
            if current < target:
                l += 1
            elif current > target:
                r -= 1
            else:
                return [l + 1, r + 1]
