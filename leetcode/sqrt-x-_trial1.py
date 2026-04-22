class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        low, high = 1, x // 2
        ans = 1
        while low <= high:
            mid = (low + high) // 2
            sqr = mid * mid
            if sqr == x:
                return mid
            
            if sqr < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans