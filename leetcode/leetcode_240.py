# https://leetcode.com/problems/search-a-2d-matrix-ii/
# leetcode 240 : Search a 2D Matrix II
# LEVEL : Medium

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        r, c = 0, n-1

        while 0 <= r < m and 0 <= c < n:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            else:
                c -= 1

        return False
