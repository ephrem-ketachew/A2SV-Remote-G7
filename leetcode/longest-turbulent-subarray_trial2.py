class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        max_len = 0
        for right in range(len(arr) - 1):
            if right % 2 == 1:
                if arr[right] <= arr[right + 1]:
                    left = right + 1
            if right % 2 == 0:
                if arr[right] >= arr[right + 1]:
                    left = right + 1
                    
            max_len = max(max_len, right - left + 1)
             
        left = 0
        for right in range(len(arr) - 1):
            if right % 2 == 1:
                if arr[right] >= arr[right + 1]:
                    left = right + 1
            if right % 2 == 0:
                if arr[right] <= arr[right + 1]:
                    left = right + 1
                    
            max_len = max(max_len, right - left + 1)
            
        return max_len + 1