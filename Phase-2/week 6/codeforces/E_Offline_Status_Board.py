import sys

input = sys.stdin.readline

t = int(input())

output = []
for _ in range(t):
    n = int(input())
    
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    def is_subsequence(s: list, t: list) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
            
        return j == len(t)
    
    low = 0
    high = n - 1
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        is_sub = is_subsequence(arr1, arr2[mid:])
        
        if is_sub:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
                
    output.append(str(ans))
    
print('\n'.join(output))