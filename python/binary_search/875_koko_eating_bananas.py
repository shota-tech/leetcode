# https://leetcode.com/problems/koko-eating-bananas/

import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        ng = 0
        ok = max(piles)

        while ok - ng > 1:
            k = ng + (ok - ng) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            if hours <= h:
                ok = k
            else:
                ng = k

        return ok
