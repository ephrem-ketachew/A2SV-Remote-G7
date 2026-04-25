import sys 

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    if n == 1:
        print('YES')
        continue
    
    x, y = arr[0], arr[1]
    
    b = (2 * x  - y) // (n + 1)
    a = x - n * b
    
    if a < 0 or b < 0:
        print('NO')
        continue
    
    can_explode = True
    for i, num in enumerate(arr):
        if num - ((i + 1) * a + (n - i) * b) != 0:
            can_explode = False
            break
        
    if can_explode:
        print('YES')
    else:
        print('NO')