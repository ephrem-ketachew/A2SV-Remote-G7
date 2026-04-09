class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        arr = [-1] * n
        stack = []
        for i, num in enumerate(nums2):
            while stack and num > nums2[stack[-1]]:
                idx = stack.pop()
                arr[idx] = num
            stack.append(i)
            
        ans = [-1] * len(nums1)
        map_idx = {}
        for i, num in enumerate(nums2):
            map_idx[num] = i
        
        for i, num in enumerate(nums1):
            idx = map_idx[num]
            ans[i] = arr[idx]
            
        return ans