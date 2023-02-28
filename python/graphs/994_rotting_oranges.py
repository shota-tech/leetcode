# https://leetcode.com/problems/rotting-oranges/

from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        q = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row, col))

        time = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (
                        r < 0 or rows <= r
                        or c < 0 or cols <= c
                        or grid[r][c] != 1
                    ):
                        continue

                    grid[r][c] = 2
                    fresh -= 1
                    q.append((r, c))
            time += 1

        return time if not fresh else -1
