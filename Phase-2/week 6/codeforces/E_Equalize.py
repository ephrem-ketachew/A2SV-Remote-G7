import sys 

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    sorted_uniques = sorted(set(arr))
    max_len = 0
    left = 0
    for right in range(len(sorted_uniques)):
        while sorted_uniques[right] - sorted_uniques[left] > n - 1:
            left += 1
            
        max_len = max(max_len, right - left + 1)
        
    output.append(str(max_len))
    
print('\n'.join(output))