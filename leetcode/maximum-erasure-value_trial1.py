class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counter = Counter()
        left = 0
        max_score = 0
        win_sum = 0
        for right in range(len(nums)):
            counter[nums[right]] += 1
            win_sum += nums[right]
            
            while counter[nums[right]] > 1:
                counter[nums[left]] -= 1
                win_sum -= nums[left]
                left += 1
                
            max_score = max(max_score, win_sum)
            
        return max_score