class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * (n + 1)
            
        for start, end, direction in shifts:
            if direction == 0:
                prefix[start] -= 1
                prefix[end + 1] += 1
            else:
                prefix[start] += 1
                prefix[end + 1] -= 1
                
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + prefix[i]
        
        new_s = []
        for i in range(n):
            prev = ord(s[i]) - 97
            now = 97 + (prefix[i] + prev) % 26
            new_s.append(chr(now))
            
        return ''.join(new_s)