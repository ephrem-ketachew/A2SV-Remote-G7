class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = right = 0
        n = len(nums)
        while right < n:
            while right + 1 < n and nums[right] == nums[right + 1]:
                right += 1

            nums[left] = nums[right]
            left += 1
            right += 1

        return left
