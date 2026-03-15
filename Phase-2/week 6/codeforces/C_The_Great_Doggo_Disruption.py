n = int(input())
s = input().strip()

if n == 1 or len(set(s)) < n:
    print('Yes')
else:
    print('No')

