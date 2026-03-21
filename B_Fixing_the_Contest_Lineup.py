import sys 

input = sys.stdin.readline

n = int(input())
output = []
for _ in range(n):
    n = int(input())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    i = j = 0
    while i < n and j < n:
        if a[i] <= b[j]:
            i += 1
        j += 1
        
    output.append(str(n - i))
    
print('\n'.join(output))