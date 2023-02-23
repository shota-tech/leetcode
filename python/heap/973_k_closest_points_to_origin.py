# https://leetcode.com/problems/k-closest-points-to-origin/

import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        min_heap = []
        for x, y in points:
            distance = x ** 2 + y ** 2
            min_heap.append((distance, x, y))
        heapq.heapify(min_heap)

        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(min_heap)
            res.append([x, y])

        return res
