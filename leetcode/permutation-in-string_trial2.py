class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k, n = len(s1), len(s2)
        
        if n < k:
            return False
        
        counter_s1 = Counter(s1)
        counter_win = Counter()

        formed = 0
        need = len(counter_s1)
        
        for right in range(k):
            counter_win[s2[right]] += 1
            if counter_s1[s2[right]] == counter_win[s2[right]]:
                formed += 1
                
        if formed == need:
            return True
        
        for right in range(k, n):
            if counter_win[s2[right - k]] == counter_s1[s2[right - k]]:
                formed -= 1
                
            counter_win[s2[right - k]] -= 1

            counter_win[s2[right]] += 1
            
            if counter_s1[s2[right]] == counter_win[s2[right]]:
                formed += 1
                
            if formed == need:
                return True
            
        return False
            