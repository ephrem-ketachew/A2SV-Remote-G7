import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

sereja = dima = 0
turn = 0
left, right = 0, len(arr) - 1
while left <= right:
    if arr[left] >= arr[right]:
        s = arr[left]
        left += 1
    else:
        s = arr[right]
        right -= 1
        
    if turn == 0:
        sereja += s
    else:
        dima += s
        
    turn ^= 1
    
print(f'{sereja} {dima}')