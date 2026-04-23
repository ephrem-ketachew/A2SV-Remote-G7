n, d = map(int, input().split())
p = list(map(int, input().split()))

p.sort()

left, right = 0, n - 1
count = 0
while left <= right:
    curr = p[right]
    while curr <= d and left < right:
        curr += p[right]
        left += 1
        
    if curr > d:
        count += 1
        
    right -= 1
    
print(count)