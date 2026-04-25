class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low, high = 0, position[-1]
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            left = 0
            count = 1
            for right in range(len(position)):
                if position[right] - position[left] >= mid:
                    count += 1
                    left = right
            if count >= m:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans