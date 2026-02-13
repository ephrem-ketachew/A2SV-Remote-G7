# 54. Spiral Matrix
# Medium

# Given an m x n matrix, return all elements of the matrix in spiral order.


# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        top_left, top_right, bot_left, bot_right = [0, 0], [0, n - 1], [m - 1, 0], [m - 1, n - 1]
        while top_left[1] <= top_right[1] and top_left[0] <= bot_left[0]:
            y_start, y_end = top_left[1], top_right[1]
            x = top_left[0]
            for j in range(y_start, y_end + 1):
                ans.append(matrix[x][j])
  
            x_start, x_end = top_right[0], bot_right[0]
            y = top_right[1]
            for i in range(x_start + 1, x_end + 1):
                ans.append(matrix[i][y])

            if top_left[0] < bot_left[0]:
                x = bot_left[0] 
                for j in range(y_end - 1, y_start - 1, - 1):
                    ans.append(matrix[x][j])
                
            if top_right[1] > top_left[1]:
                y = top_left[1]
                for i in range(x_end - 1, x_start, - 1):
                    ans.append(matrix[i][y])

            top_left = top_left[0] + 1, top_left[1] + 1
            top_right = top_right[0] + 1, top_right[1] - 1
            bot_left = bot_left[0] - 1, bot_left[1] + 1
            bot_right = bot_right[0] - 1, bot_right[1] - 1
            
        return ans