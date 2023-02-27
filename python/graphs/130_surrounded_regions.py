# https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def dfs(row: int, col: int):
            if (
                row < 0 or rows <= row
                or col < 0 or cols <= col
                or board[row][col] != 'O'
            ):
                return

            board[row][col] = '#'
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols - 1)

        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == '#':
                    board[row][col] = 'O'
