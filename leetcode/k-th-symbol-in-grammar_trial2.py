class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        m = (2 ** (n - 1)) // 2
        if k <= m:
            return self.kthGrammar(n - 1, k)
        
        return 1 ^ self.kthGrammar(n - 1, k - m)