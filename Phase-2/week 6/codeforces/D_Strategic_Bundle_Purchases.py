import sys

input = sys.stdin.readline

t = int(input())

output = []
for _ in range(t):
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))
    coupons = list(map(int, input().split()))
    
    prices.sort(reverse=True)
    coupons.sort()
    
    i = j = 0
    cost = 0
    while i < n and j < k:
        if i + coupons[j] > n:
            break
        x = coupons[j]
        while x > 1:
            cost += prices[i]
            i += 1
            x -= 1
            
        i += 1
        j += 1
        
    while i < n:
        cost += prices[i]
        i += 1
        
    output.append(str(cost))
    
print('\n'.join(output))
        