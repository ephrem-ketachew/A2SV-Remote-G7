# 498. Diagonal Traverse
# Medium
# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

# Example 1:

# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# Example 2:

# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
 
# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# -105 <= mat[i][j] <= 105

from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(mat), len(mat[0])
        dir = 1
        for k in range(n):
            temp = []
            i, j = 0, k
            while j >= 0 and i < m:
                temp.append(mat[i][j])
                j -= 1
                i += 1
                
            if dir == 1:
                temp.reverse()
            
            ans.extend(temp)
            
            dir ^= 1
            
        for k in range(1, m):
            temp = []
            i, j = k, n - 1
            while i < m and j >= 0:
                temp.append(mat[i][j])
                i += 1
                j -= 1
                
            if dir == 1:
                temp.reverse()
                
            ans.extend(temp)
            
            dir ^= 1   
            
        return ans