class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = bisect_right(matrix, target, key=lambda row: row[0]) - 1
        j = bisect_left(matrix[i], target)
        
        return j < len(matrix[0]) and matrix[i][j] == target