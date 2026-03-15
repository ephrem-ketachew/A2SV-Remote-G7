class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most(k: int) -> int:
            count = 0
            odd_cnt = 0
            left = 0
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd_cnt += 1
                    
                while odd_cnt > k:
                    if nums[left] % 2 == 1:
                        odd_cnt -= 1
                    left += 1
                    
                count += right - left + 1
                
            return count
        
        return at_most(k) - at_most(k - 1)