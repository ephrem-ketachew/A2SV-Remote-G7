n = int(input())

nums = list(map(int, input().split()))
sereja_points = 0
dima_points = 0

left, right = 0, n - 1
current_player = 0
while left <= right:
    max_point = max(nums[left], nums[right])
    if nums[left] >= nums[right]:
        left += 1
    else:
        right -= 1
    
    if current_player == 0:
        sereja_points += max_point
    else:
        dima_points += max_point
        
    current_player ^= 1
    
print(f'{sereja_points} {dima_points}')