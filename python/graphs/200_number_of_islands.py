# https://leetcode.com/problems/number-of-islands/

from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        island = 0

        def bfs(row: int, col: int):
            q = deque()
            q.append((row, col))
            visit.add((row, col))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (
                        0 <= r < rows
                        and 0 <= c < cols
                        and grid[r][c] == '1'
                        and (r, c) not in visit
                    ):
                        q.append((r, c))
                        visit.add((r, c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visit:
                    bfs(row, col)
                    island += 1

        return island
