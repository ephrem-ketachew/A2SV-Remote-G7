import sys 

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    min_ch = s[0]
    min_idx = 0
    for i, ch in enumerate(s):
        if ch <= min_ch:
            min_idx = i
            min_ch = ch
            
    arr = list(s)
    ch = arr.pop(min_idx)
    arr = [ch] + arr
    
    output.append(''.join(arr))
    
print('\n'.join(output))
            