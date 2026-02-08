import sys

input = sys.stdin.read
data = input().split()
iterator = iter(data)

t = int(next(iterator))
result = []
for _ in range(t):
    n = int(next(iterator))
    nums = [int(next(iterator)) for _ in range(n)]
    
    odds = [num for num in nums if num % 2 == 1]
    evens = [num for num in nums if num % 2 == 0]
            
    odds.sort(reverse=True)
    evens.sort(reverse=True)
    
    pref = [0] * (len(evens) + 1)
    for i in range(len(evens)):
        pref[i + 1] = evens[i] + pref[i]
    
    ans = []
    for k in range(1, n + 1):
        m = max(1, k - len(evens))
        if m % 2 == 0:
            m += 1
            
        if len(odds) < m or m > k:
            ans.append('0')
        else:
            summ = odds[0] + pref[k - m]
            ans.append(str(summ))
            
    result.append(' '.join(ans))
    
print('\n'.join(result))