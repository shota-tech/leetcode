# https://leetcode.com/problems/time-based-key-value-store/

from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        if not len(values):
            return ''

        ok = -1
        ng = len(values)
        while ng - ok > 1:
            m = ok + (ng - ok) // 2
            if values[m][1] <= timestamp:
                ok = m
            else:
                ng = m

        return values[ok][0] if ok != -1 else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
