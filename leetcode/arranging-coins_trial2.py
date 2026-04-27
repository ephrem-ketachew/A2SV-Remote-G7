class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 1, n
        while low < high:
            rows = (low + high + 1) // 2
            coins_needed = rows * (rows + 1) // 2
            if coins_needed <= n:
                low = rows
            else:
                high = rows - 1
                
        return low
