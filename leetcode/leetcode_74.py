# https://leetcode.com/problems/search-a-2d-matrix/
# leetcode 74 : Search a 2D Matrix
# LEVEL : Medium

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        
        start, end = 0, row*col-1
        while start <= end:
            mid = (start + end) // 2
            r, c = mid // col, mid % col
            
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return False