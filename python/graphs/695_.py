# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(row: int, col: int) -> int:
            if (
                row < 0 or rows <= row
                or col < 0 or cols <= col
                or grid[row][col] == '0'
                or (row, col) in visit
            ):
                return 0

            visit.add((row, col))

            return (
                1 + dfs(row - 1, col)
                + dfs(row + 1, col)
                + dfs(row, col - 1)
                + dfs(row, col + 1)
            )

        area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visit:
                    area = max(area, dfs(row, col))

        return area
