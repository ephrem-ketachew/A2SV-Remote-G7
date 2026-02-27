class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        counter = Counter(arr1)
        for num in arr2:
            ans.extend([num] * counter[num])

        remaining = []
        arr2_set = set(arr2)
        for num in arr1:
            if num not in arr2_set:
                remaining.append(num)
        
        remaining.sort()

        return ans + remaining