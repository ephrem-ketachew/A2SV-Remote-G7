class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        unique_nums = sorted(set(nums))
        
        max_built = 0
        for i, num in enumerate(unique_nums):
            end = num + n - 1
            end_idx = bisect.bisect_right(unique_nums, end)
            
            cur_built = end_idx - i
            
            max_built = max(max_built, cur_built)
            
        return n - max_built