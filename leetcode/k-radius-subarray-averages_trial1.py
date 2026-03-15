class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        diameter = 2 * k + 1
        if diameter > n:
            return [-1] * n
        
        ans = [-1] * n
        win_sum = sum(nums[:diameter])
        ans[k] = win_sum // diameter
        for i in range(k + 1, n - k):
            win_sum += nums[i + k] - nums[i - k - 1]
            ans[i] = win_sum // diameter
        
        return ans
        