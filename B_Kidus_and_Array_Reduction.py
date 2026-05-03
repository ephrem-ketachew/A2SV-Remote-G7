import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    maxx = 0
    count = 0
    for i, num in enumerate(a):
        if num > maxx or num == maxx:
            maxx = num
            count += 1
            
    print(count)