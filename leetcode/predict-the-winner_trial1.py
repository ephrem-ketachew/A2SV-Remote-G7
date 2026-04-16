class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        total = sum(nums)
        def helper(left: int, right: int, first: int, score: int) -> bool:
            if left > right:
                return score >= total - score
            
            if first == 0:
                return helper(left + 1, right, 1, score + nums[left]) or helper(left, right - 1, 1, score + nums[right])
            
            return helper(left + 1, right, 0, score) and helper(left, right - 1, 0, score) 
        
        return helper(0, len(nums) - 1, 0, 0)