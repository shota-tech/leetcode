# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(row: int, col: int, prev: int, visit: set[tuple[int]]):
            if (
                row < 0 or rows <= row
                or col < 0 or cols <= col
                or heights[row][col] < prev
                or (row, col) in visit
            ):
                return

            visit.add((row, col))
            dfs(row - 1, col, heights[row][col], visit)
            dfs(row + 1, col, heights[row][col], visit)
            dfs(row, col - 1, heights[row][col], visit)
            dfs(row, col + 1, heights[row][col], visit)

        for row in range(rows):
            dfs(row, 0, 0, pacific)
            dfs(row, cols - 1, 0, atlantic)

        for col in range(cols):
            dfs(0, col, 0, pacific)
            dfs(rows - 1, col, 0, atlantic)

        res = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])
        return res
