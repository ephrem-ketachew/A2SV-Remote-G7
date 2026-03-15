from collections import Counter
from typing import List

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        
        q = s.count('Q')
        w = s.count('W')
        e = s.count('E')
        r = s.count('R')
        
        need = n // 4
        
        more_q = max(0, q - need)
        more_w = max(0, w - need)
        more_e = max(0, e - need)
        more_r = max(0, r - need)
        
        more = 'Q' * more_q + 'W' * more_w + 'E' * more_e + 'R' * more_r
        
        surplus = Counter(more)

        min_len = n
        counter = Counter()
        left = 0
        
        need = len(surplus)
        formed = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            
            if counter[s[right]] == surplus[s[right]]:
                formed += 1
            
            while left <= right and counter[s[left]] > surplus[s[left]]:
                counter[s[left]] -= 1
                left += 1

            if formed == need:
                min_len = min(min_len, right - left + 1)
                
        return min_len