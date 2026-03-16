class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most_k(k: int) -> int:
            counter = Counter()
            count = left = 0
            for right in range(len(nums)):
                counter[nums[right]] += 1
                while len(counter) > k:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        del counter[nums[left]]
                    left += 1
                    
                count += right - left + 1
                
            return count
        
        return at_most_k(k) - at_most_k(k - 1)