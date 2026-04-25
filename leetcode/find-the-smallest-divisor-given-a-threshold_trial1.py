class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)
        while low < high:
            mid = (low + high) // 2
            s = 0
            for num in nums:
                s += (num + mid - 1) // mid
                
            if s <= threshold:
                high = mid
            else:
                low = mid + 1
                
        return low