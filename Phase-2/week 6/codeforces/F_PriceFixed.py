import sys 

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
    
arr.sort(key=lambda x: x[1])

left = 0
right = n - 1
cost = 0
bought = 0
while left <= right:
    if arr[left][1] <= bought:
        bought += arr[left][0]
        cost += arr[left][0]
        left += 1
    else:
        needed = arr[left][1] - bought
        take = min(needed, arr[right][0])
        
        bought += take
        cost += 2 * take
        arr[right][0] -= take
        if arr[right][0] == 0:
            right -= 1
            
print(str(cost))