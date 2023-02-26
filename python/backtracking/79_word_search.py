# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visit = set()

        def dfs(row: int, col: int, i: int) -> bool:
            if i == len(word):
                return True

            if (
                row < 0 or rows <= row
                or col < 0 or cols <= col
                or board[row][col] != word[i]
                or (row, col) in visit
            ):
                return False

            visit.add((row, col))
            res = (
                dfs(row - 1, col, i + 1)
                or dfs(row + 1, col, i + 1)
                or dfs(row, col - 1, i + 1)
                or dfs(row, col + 1, i + 1)
            )
            visit.remove((row, col))
            return res

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False
