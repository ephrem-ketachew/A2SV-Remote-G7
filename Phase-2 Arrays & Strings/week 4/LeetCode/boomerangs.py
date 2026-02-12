# 447. Number of Boomerangs
# Medium

# You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

# Return the number of boomerangs.

# Example 1:

# Input: points = [[0,0],[1,0],[2,0]]
# Output: 2
# Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].
# Example 2:

# Input: points = [[1,1],[2,2],[3,3]]
# Output: 2
# Example 3:

# Input: points = [[1,1]]
# Output: 0
 

# Constraints:

# n == points.length
# 1 <= n <= 500
# points[i].length == 2
# -104 <= xi, yi <= 104
# All the points are unique.

from typing import List
from collections import Counter

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        # count = 0
        # for i in range(len(points) - 2):
        #     for j in range(i + 1, len(points) - 1):
        #         for k in range(j + 1, len(points)):
        #             # case1 i appears first
        #             dist_ij = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
        #             dist_ik = (points[i][0] - points[k][0]) ** 2 + (points[i][1] - points[k][1]) ** 2
                    
        #             if dist_ij == dist_ik:
        #                 count += 2
                        
        #             # case 2 j appears first
        #             dist_ji = (points[j][0] - points[i][0]) ** 2 + (points[j][1] - points[i][1]) ** 2
        #             dist_jk = (points[j][0] - points[k][0]) ** 2 + (points[j][1] - points[k][1]) ** 2
                    
        #             if dist_ji == dist_jk:
        #                 count += 2
                        
        #             # case 3 k appears first
        #             dist_ki = (points[k][0] - points[i][0]) ** 2 + (points[k][1] - points[i][1]) ** 2
        #             dist_kj = (points[k][0] - points[j][0]) ** 2 + (points[k][1] - points[j][1]) ** 2
                    
        #             if dist_ki == dist_kj:
        #                 count += 2
                    
                        
        # return count
        
        count = 0
        for i in range(len(points)):
            counter = Counter()
            for j in range(len(points)):
                distance = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                counter[distance] += 1
                
            for key in counter:
                freq = counter[key]
                count += freq * (freq - 1)

        return count
                
            
                
        