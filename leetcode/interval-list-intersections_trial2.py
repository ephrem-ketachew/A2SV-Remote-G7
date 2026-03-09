class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            f_start, f_end = firstList[i]
            s_start, s_end = secondList[j]

            if f_start <= s_start:
                if s_start <= f_end:
                    ans.append([s_start, min(f_end, s_end)])
            else:
                if f_start <= s_end:
                    ans.append([f_start, min(f_end, s_end)])
                    
            if f_end <= s_end:
                i += 1
            else:
                j += 1
                
        return ans