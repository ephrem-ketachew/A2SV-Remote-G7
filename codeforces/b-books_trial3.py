n, t = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]
    
max_books = 0
left = 0
for right in range(1, n + 1):
    while prefix[right] - prefix[left] > t:
        left += 1
        
    max_books = max(max_books, right - left)
    
print(max_books)