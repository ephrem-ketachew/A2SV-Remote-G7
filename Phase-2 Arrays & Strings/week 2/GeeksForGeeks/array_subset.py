# Array Subset
# Difficulty: BasicAccuracy: 44.05%Submissions: 516K+Points: 1Average Time: 20m
# Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

# Examples:

# Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
# Output: true
# Explanation: b[] is a subset of a[]
# Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
# Output: true
# Explanation: b[] is a subset of a[]
# Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
# Output: false
# Explanation: b[] is not a subset of a[]
# Constraints:
# 1 <= a.size(), b.size() <= 105
# 1 <= a[i], b[j] <= 106

#User function Template for python3

from collections import Counter

class Solution:
    def isSubset(self, a, b):
        if len(a) < len(b):
            return False
        counter_a = Counter(a)
        counter_b = Counter(b)
        
        for num in counter_b:
            if counter_a[num] < counter_b[num]:
                return False
            
        return True
        
        