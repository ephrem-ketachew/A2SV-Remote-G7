class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        
        left, right = 0, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s < target:
                count += right - left
                left += 1
            else:
                right -= 1
                
        return count