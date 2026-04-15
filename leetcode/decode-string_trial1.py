class Solution:
    def decodeString(self, s: str) -> str:
        decoded = ''
        i, n = 0, len(s)
        num = 1
        while i < n:
            if s[i].isnumeric():
                digits = []
                while s[i].isnumeric():
                    digits.append(s[i])
                    i += 1
                num = int(''.join(digits))
            elif s[i].islower():
                chars = []
                while i < n and s[i].islower():
                    chars.append(s[i])
                    i += 1
                decoded += num * ''.join(chars)
                num = 1
            else:
                encoded = []
                opn = 1
                i += 1
                while opn > 0:
                    encoded.append(s[i])
                    if s[i] == ']':
                        opn -= 1
                    elif s[i] == '[':
                        opn += 1
                    i += 1
                    
                encoded.pop()
                    
                decoded += num * self.decodeString(''.join(encoded))
                num = 1
                
        return decoded