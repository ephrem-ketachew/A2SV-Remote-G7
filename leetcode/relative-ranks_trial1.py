class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_idx = [(num, idx) for idx, num in enumerate(score)]
        score_idx.sort(reverse=True)
        
        ans = [0] * len(score)
        for rank, (score, idx) in enumerate(score_idx, start=1):
            if rank == 1:
                ans[idx] = 'Gold Medal'
            elif rank == 2:
                ans[idx] = 'Silver Medal'
            elif rank == 3:
                ans[idx] = 'Bronze Medal'
            else:
                ans[idx] = str(rank)
                
        return ans