class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        closest_sum = float('inf')
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == target:
                    return target
                elif s < target:
                    left += 1
                else:
                    right -= 1
                    
                if abs(s - target) < min_diff:
                    closest_sum = s
                    min_diff = abs(s - target)
                    
        return closest_sum