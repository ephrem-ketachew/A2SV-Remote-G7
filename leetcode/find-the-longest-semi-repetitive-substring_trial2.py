class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        repeat_count = 0
        max_len = 1
        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                repeat_count += 1
            while repeat_count > 1:
                if s[left] == s[left + 1]:
                    repeat_count -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len