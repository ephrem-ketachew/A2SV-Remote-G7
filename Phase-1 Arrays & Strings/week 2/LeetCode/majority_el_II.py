# 229. Majority Element II
# Medium

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]
 
# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
 
# Follow up: Could you solve the problem in linear time and in O(1) space?

from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # counter = Counter(nums)
        # return [num for num in counter if counter[num] > len(nums) // 3]
        
        cand1 = cand2 = None
        count1 = count2 = 0
        
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
                
        count1 = count2 = 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
        
        res = []
        print(count1, count2)
        if count1 > len(nums) // 3:
            res.append(cand1)
        if count2 > len(nums) // 3:
            res.append(cand2)
            
        return res