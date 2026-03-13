class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def is_valid(counter: Counter) -> bool:
            max_freq = 0
            total = 0
            for ch in counter:
                total += counter[ch]
                if counter[ch] > max_freq:
                    max_freq = counter[ch]
                    
            return total - max_freq <= k
        
        counter = Counter()
        left = 0
        max_len = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            
            while not is_valid(counter):
                counter[s[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len
        
        