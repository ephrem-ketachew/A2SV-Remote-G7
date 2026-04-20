class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, num in enumerate(nums):
            if not stack or num <= nums[stack[-1]]:
                stack.append(i)
                
        max_len = 0
        for i in range(len(nums) - 1, -1, -1):
            j = i
            while stack and nums[stack[-1]] <= nums[i]:
                j = stack.pop()
            
            max_len = max(max_len, i - j)
            
        return max_len