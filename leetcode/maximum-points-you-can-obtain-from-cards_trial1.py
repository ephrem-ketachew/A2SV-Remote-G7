class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        remain = len(cardPoints) - k
        min_sum = win_sum = sum(cardPoints[:remain])
        for i in range(remain, len(cardPoints)):
            win_sum += cardPoints[i] - cardPoints[i - remain]
            min_sum = min(min_sum, win_sum)
            
        return sum(cardPoints) - min_sum