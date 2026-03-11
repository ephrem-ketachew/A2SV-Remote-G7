class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        ans = []
        p_counter = Counter(p)
        win_counter = Counter()
        for right in range(len(s)):
            win_counter[s[right]] += 1
            while win_counter[s[right]] > p_counter[s[right]]:
                win_counter[s[left]] -= 1
                if win_counter[s[left]] == 0:
                    del win_counter[s[left]]
                left += 1
                
            if right - left + 1 == len(p):
                ans.append(left)
                
        return ans