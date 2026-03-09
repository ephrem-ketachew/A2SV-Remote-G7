class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    pairs = [nums[i], nums[left], nums[right]]
                    ans.append(pairs)
                    
                    l = nums[left]
                    while left < len(nums) and nums[left] == l:
                        left += 1
                        
                    r = nums[right]
                    while right >= 0 and nums[right] == r:
                        right -= 1
                elif s > target:
                    right -= 1
                else:
                    left += 1
                    
        return ans