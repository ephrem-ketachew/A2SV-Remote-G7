class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        is_neg = n < 0
        n = abs(n)
        half = int(n / 2)
        res = self.myPow(x * x, half)
        if n % 2 == 1:
            res *= x
            
        if is_neg:
            res = 1 / res
            
        return res