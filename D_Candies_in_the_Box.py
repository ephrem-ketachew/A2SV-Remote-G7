n, k = map(int, input().split())

total = n * (n + 1) // 2
count = 0
r = n
while total > k:
    total -= (r + 1)
    r -= 1
    count += 1

print(count)