# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bottom = rows - 1

        while top <= bottom:
            row = top + (bottom - top) // 2
            if matrix[row][0] > target:
                bottom = row - 1
            elif matrix[row][cols - 1] < target:
                top = row + 1
            else:
                break

        if top > bottom:
            return False

        row = top + (bottom - top) // 2
        l = 0
        r = cols - 1
        while l <= r:
            col = l + (r - l) // 2
            if matrix[row][col] > target:
                r = col - 1
            elif matrix[row][col] < target:
                l = col + 1
            else:
                return True

        return False
