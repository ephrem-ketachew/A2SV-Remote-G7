class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = nums[i] + suffix[i + 1]
            
        prefix = 0
        for i in range(n):
            if prefix == suffix[i + 1]:
                return i
            prefix += nums[i]
            
        return -1