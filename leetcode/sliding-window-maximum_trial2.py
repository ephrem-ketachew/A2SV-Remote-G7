class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)
        queue = deque()
        for i in range(k):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            
        ans[0] = nums[queue[0]]
        for i in range(k, n):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            
            while i - queue[0] + 1 > k:
                queue.popleft()
  
            ans[i - k + 1] = nums[queue[0]]
            
        return ans