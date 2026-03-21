class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = Counter()
        seen[0] = -1
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            remainder = prefix % k
            if remainder in seen:
                idx = seen[remainder]
                if i - idx >= 2:
                    return True
            else:
                seen[remainder] = i

        return False