import sys 

input = sys.stdin.readline

n, m = map(int, input().split())
left, right = n + 1, 0

for _ in range(m):
    clue = input().strip()
    
    idx = int(clue.split()[-1])
    
    if 'left' in clue:
        left = min(left, idx)
    else:
        right = max(right, idx)
        
        
if left - right <= 1:
    loc_count = -1
else:
    loc_count = left - right - 1
        
print(loc_count)