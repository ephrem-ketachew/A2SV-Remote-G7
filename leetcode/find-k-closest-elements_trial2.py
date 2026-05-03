class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect.bisect_left(arr, x)
        if 0 < idx < len(arr) and abs(arr[idx - 1] - x) <= abs(arr[idx] - x):
            idx -= 1

        if idx == len(arr):
            idx -= 1
            
        ans = []
        left, right = idx, idx + 1
        while len(ans) < k:
            if left < 0:
                ans.append(arr[right])
                right += 1
            elif right >= len(arr):
                ans.append(arr[left])
                left -= 1
            else:    
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    ans.append(arr[left])
                    left -= 1
                else:
                    ans.append(arr[right])
                    right += 1

        ans.sort() 
        return ans