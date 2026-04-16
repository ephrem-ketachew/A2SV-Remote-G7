class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # arr = list(range(1, n + 1))
        # idx = 0
        # while len(arr) > 1:
        #     idx = (idx + k - 1) % len(arr)
        #     arr.remove(arr[idx])
        #     idx %= len(arr)
            
        # return arr[0]
        
        def winner(n: int) -> int:
            if n == 1:
                return 0
            
            return (winner(n - 1) + k) % n
        
        return winner(n) + 1