class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = Counter()
        left = 0
        max_len = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            while counter[s[right]] > 1:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len