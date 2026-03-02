class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set = list(set(nums))
        nums_set.sort(reverse=True)
        return nums_set[2] if len(nums_set) >= 3 else nums_set[0]