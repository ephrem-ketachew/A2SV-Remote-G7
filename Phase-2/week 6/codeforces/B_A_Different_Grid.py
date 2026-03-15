import sys 

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        row = list(input().split())
        a.append(row)
        
    if n == m == 1:
        output.append('-1')
        continue
    
    if m == 1:
        new_mat = a[1:] + [a[0]]
        
        for i in range(n):
            output.append(new_mat[i][0])
            
        continue
    
    b = []
    for row in a:
        new_row = row[1:] + [row[0]]
        output.append(' '.join(new_row))
        
print('\n'.join(output))
        
        
        