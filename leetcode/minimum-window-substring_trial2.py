class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_subseq(counter: Counter, t_counter: Counter) -> bool:
            for ch in t_counter:
                if counter[ch] < t_counter[ch]:
                    return False
                
            return True
        
        t_counter = Counter(t)
        win_counter = Counter()
        min_win_bound = (0, 0)
        min_len = float('inf')
        left = 0
        for right in range(len(s)):
            win_counter[s[right]] += 1
            
            while left < len(s) and win_counter[s[left]] > t_counter[s[left]]:
                win_counter[s[left]] -= 1
                if win_counter[s[left]] == 0:
                    del win_counter[s[left]]
                left += 1
                
            if is_subseq(win_counter, t_counter) and right - left + 1 < min_len:
                min_len = right - left + 1
                min_win_bound = (left, right)
                
        left, right = min_win_bound
        
        return s[left:right + 1] if min_len != float('inf') else ''
                
                