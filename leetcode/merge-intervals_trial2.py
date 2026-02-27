class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            prev_start, prev_end = ans[-1]
            start, end = intervals[i]
            if prev_end >= start:
                ans.pop()
                ans.append([prev_start, max(prev_end, end)])
            else:
                ans.append([start, end])

        return ans