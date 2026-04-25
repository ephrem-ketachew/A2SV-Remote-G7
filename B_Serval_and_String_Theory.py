import sys 

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    
    arr = list(s)
    sorted_arr = sorted(arr)
    
    ops = min(n - 1, k)
    i = 0
    while k > 0 and i < n:
        while i < n and arr[i] == sorted_arr[i]:
            i += 1
        
        if i < n:
            ch = sorted_arr[i]
            for j in range(n - 1, i, -1):
                if arr[j] == ch:
                    break
                
            arr[i], arr[j] = arr[j], arr[i]
            
    my_s = ''.join(arr)
    arr.reverse()
    rev_s = ''.join(arr)
    
    if my_s < rev_s:
        print('YES')
    else:
        print('NO')