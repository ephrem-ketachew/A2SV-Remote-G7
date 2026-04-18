import sys 

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        output.append('0')
        continue
    
    output.append(str(n - 1))
    ops = []
    x = -1
    if (a[0] % 2 == 0 and a[-1] % 2 == 0) or (a[0] % 2 == 1 and a[-1] % 2 == 1):
        x = a[-1]
    else:
        x = a[0]
        
    ops.append(f'{1} {n}')
    
    for i in range(1, n - 1):
        if a[i] % 2 == 0:
            if x % 2 == 0:
                ops.append(f'{i + 1} {n}')
            else:
                ops.append(f'{1} {i + 1}')
        else:
            if x % 2 == 0:
                ops.append(f'{1} {i + 1}')
            else:
                ops.append(f'{i + 1} {n}')
                
    output.append('\n'.join(ops))
    
print('\n'.join(output))
                