class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        left = 0
        count = 0
        curr_pdt = 1
        for right in range(len(nums)):
            curr_pdt *= nums[right]
            while left <= right and curr_pdt >= k:
                curr_pdt //= nums[left]
                left += 1
                
            count += right - left + 1
            
        return count