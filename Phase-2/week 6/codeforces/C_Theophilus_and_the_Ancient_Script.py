import sys

input = sys.stdin.readline

t = int(input())

output = []
for _ in range(t):
    n = int(input())
    s = input()
    
    ops = 0
    a_cnt = 0
    for i in range(n):
        if s[i] == 'A':
            a_cnt += 1
        else:
            if a_cnt > 0:
                ops += a_cnt
                a_cnt = 1
                
    output.append(str(ops))
    
print('\n'.join(output))