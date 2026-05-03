import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    impressions = []
    max_num = 0
    for _ in range(n):
        l, r = map(int, input().split())
        impressions.append((l, r))
        max_num = max(max_num, r)
      
    prefix = [0] * (max_num + 1)
    uniques = [0] * (max_num + 1)
    counter = [0] * (max_num + 1)
    for l, r in impressions:
        if l == r:
            uniques[l] = 1
            counter[l] += 1
            
    s = 0
    for i, num in enumerate(uniques):
        s += num
        prefix[i] = s
        
    ans = ''
    for l, r in impressions:
        if l == r:
            if counter[l] == 1:
                ans += '1'
            else:
                ans += '0'
        else:
            s = prefix[r] - prefix[l - 1]
            if s == r - l + 1:
                ans += '0'
            else:
                ans += '1'
                
    print(ans)