# https://leetcode.com/problems/task-scheduler/

from collections import Counter
from collections import deque
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        q = deque()
        time = 0

        while max_heap or q:
            time += 1

            if not max_heap:
                time = q[0][1]
            else:
                cnt = heapq.heappop(max_heap)
                cnt += 1
                if cnt:
                    q.append((cnt, time + n))

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time
