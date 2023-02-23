# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l: int, r: int) -> int:
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if k < p:
                return quickSelect(l, p - 1)
            if k > p:
                return quickSelect(p + 1, r)
            return nums[p]

        return quickSelect(0, len(nums) - 1)
