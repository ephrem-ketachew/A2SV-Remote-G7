import sys 

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    for i in range(n - 1):
        if a[i] != 0:
            count += a[i]
        elif count > 0:
            count += 1
            
    output.append(str(count))
    
print('\n'.join(output))