import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    count_odds = 0
    for i in range(n):
        if a[i] % 2 == 1:
            count_odds += 1
            
    print(min(count_odds, n - count_odds))