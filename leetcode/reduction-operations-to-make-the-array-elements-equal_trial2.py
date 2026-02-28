class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(0)
        count = 0
        i, inc = 1, 1
        while i < len(nums) and nums[i] == nums[i - 1]:
            i += 1

        while i < len(nums) - 1:
            freq = 1
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                freq += 1
                i += 1
            count += freq * inc
            inc += 1
            i += 1

        return count
