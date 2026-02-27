class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_coins = 0
        left, right = 0, len(piles) - 1
        while left < right:
            right -= 1

            max_coins += piles[right]
            
            right -= 1
            left += 1

        return max_coins
