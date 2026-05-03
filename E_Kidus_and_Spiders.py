n = int(input())
a = list(map(int, input().split()))

num_nodes = 2 ** (n + 1)
light_on_road = [0] * num_nodes
light_down_road = [0] * num_nodes

for i in range(len(a)):
    light_on_road[i + 2] = a[i]
   
total_add = 0 
for intersection in range(2**n - 1, 0, -1):
    left_road = 2 * intersection
    right_road = 2 * intersection + 1
    
    light_on_left = light_on_road[left_road] + light_down_road[left_road]
    light_on_right = light_on_road[right_road] + light_down_road[right_road]
    
    total_add += abs(light_on_left - light_on_right)
    
    light_down_road[intersection] = max(light_on_left, light_on_right)
    
print(total_add)