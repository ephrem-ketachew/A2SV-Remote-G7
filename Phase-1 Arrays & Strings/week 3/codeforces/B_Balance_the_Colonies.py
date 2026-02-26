t = int(input())

for _ in range(t):
    n = int(input())
    if n <= 3:
        print(n)
    elif n % 2 == 0:
        print(0)
    else:
        print(1)