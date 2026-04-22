class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            left = nums[mid - 1] if mid > 0 else float('-inf')
            right = nums[mid + 1] if mid + 1 < len(nums) else float('-inf')
            if left < nums[mid] and nums[mid] > right:
                return mid
            
            if nums[mid] < right:
                low = mid + 1
            else:
                high = mid - 1

                