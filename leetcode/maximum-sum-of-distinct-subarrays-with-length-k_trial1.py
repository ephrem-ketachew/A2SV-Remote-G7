class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = Counter()
        win_sum = 0
        for right in range(k):
            window[nums[right]] += 1
            win_sum += nums[right]
         
        ans = 0   
        if len(window) == k:
            ans = win_sum
            
        for right in range(k, len(nums)):
            window[nums[right]] += 1
            window[nums[right - k]] -= 1
            if window[nums[right - k]] == 0:
                del window[nums[right - k]]
            
            win_sum += nums[right]
            win_sum -= nums[right - k]
            
            if len(window) == k:
                ans = max(ans, win_sum)
                
        return ans