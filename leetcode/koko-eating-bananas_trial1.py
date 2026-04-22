class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def count_hours(k: int) -> int:
            count = 0
            for pile in piles:
                count += (pile + k - 1) // k
            return count
        
        low, high = 1, max(piles)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            hours = count_hours(mid)
            if hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans