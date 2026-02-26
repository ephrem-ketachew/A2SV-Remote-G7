t = int(input())

for _ in range(t):
    n, m, p, q = map(int, input().split())
    
    if n % p == 0:
        if m == q * (n // p ):
            print('YES')
        else:
            print('NO')
    else:
        print('YES')