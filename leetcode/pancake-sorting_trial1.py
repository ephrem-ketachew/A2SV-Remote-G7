class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        for i in range(n - 1, -1, -1):
            max_idx = i
            for j in range(i - 1, -1, -1):
                if arr[j] > arr[max_idx]:
                    max_idx = j      
            if max_idx != i:
                ans.append(max_idx + 1)
                ans.append(i + 1)
                
                arr[:max_idx+1] = arr[:max_idx+1][::-1]
                arr[:i+1] = arr[:i+1][::-1]
 
        return ans