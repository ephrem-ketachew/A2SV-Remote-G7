class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        int_idx = []
        for idx, (start, end) in enumerate(intervals):
            int_idx.append((start, end, idx))
            
        int_idx.sort()
        ans = [-1] * len(intervals)
        for _, end, idx in int_idx:
            j = bisect_left(int_idx, end, key=lambda x: x[0])
            if j < len(intervals):
                ans[idx] = int_idx[j][2]
                
        return ans