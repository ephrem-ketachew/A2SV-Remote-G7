import sys

input = sys.stdin.readline

t = int(input())

output = []

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    elite_sum = arr[0]
    crowd_sum = arr[-1] + arr[-2]

    left, right = 1, n - 3
    possible = elite_sum > crowd_sum
    while left < right:
        elite_sum += arr[left]
        crowd_sum += arr[right]
        
        if elite_sum > crowd_sum:
            possible = True
            break
        
        left += 1
        right -= 1
        
    if possible:
        output.append('YES')
    else:
        output.append('NO')
        
print('\n'.join(output))
    