class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        def power(base: int, exp: int) -> int:
            if exp == 0:
                return 1
            
            half_pow = power(base, exp // 2)
            half_pow_sqr = (half_pow ** 2) % MOD
            
            if exp % 2 == 0:
                return half_pow_sqr
            else:
                return (half_pow_sqr * base) % MOD
            
        odd_count = n // 2
        even_count = n - odd_count
        
        return power(5, even_count) * power(4, odd_count) % MOD
            