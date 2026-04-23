import sys 

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    min_char = min(s)
    last_pos = s.rfind(min_char)
    new_s = s[last_pos] + s[:last_pos] + s[last_pos + 1:]
    
    output.append(new_s)
    
print('\n'.join(output))
            