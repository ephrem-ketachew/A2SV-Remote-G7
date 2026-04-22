class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find(low: int, high: int) -> int:
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            return -1
        
        left, right = 0, len(nums) - 1
        k = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                k = mid
                right = mid - 1
 
        ans = find(0, k)
        if ans != -1:
            return ans
        
        return find(k, len(nums) - 1)