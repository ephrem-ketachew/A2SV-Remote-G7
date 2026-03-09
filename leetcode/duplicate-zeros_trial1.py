class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        cnt = i = 0
        while i < n and cnt < n:
            cnt += 2 if arr[i] == 0 else 1
            i += 1

        left = i - 1
        right = n - 1
        if cnt > n:
            arr[right] = 0
            right -= 1
            left -= 1

        while left >= 0:
            if arr[left] == 0:
                arr[right] = 0
                right -= 1
            arr[right] = arr[left]
            right -= 1
            left -= 1
        
