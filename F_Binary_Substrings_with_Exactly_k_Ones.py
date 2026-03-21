import sys 

input = sys.stdin.readline

k = int(input())

s = input().strip()
n = len(s)

def at_most(r: int) -> int:
    left = right = 0
    count = 0
    one_count = 0
    while right < n:
        if s[right] == '1':
            one_count += 1
            
        while left < right and one_count > r:
            if s[left] == '1':
                one_count -= 1
            left += 1
              
        if one_count <= r:
            count += right - left + 1
        
        right += 1
        
    return count

print(at_most(k) - at_most(k - 1))