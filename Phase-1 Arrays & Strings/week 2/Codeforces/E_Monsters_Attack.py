t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    health = list(map(int, input().split()))
    pos = list(map(int, input().split()))
    
    length = max(max(pos), abs(min(pos))) + 1
    arr = [0] * length
    for i in range(len(pos)):
        x = abs(pos[i])
        y = health[i]
        arr[x] += y
     
    surplus_bullets = 0 
    win = True
    for i in range(1, length):
        if k + surplus_bullets < arr[i]:
            print('NO')
            win = False
            break
        surplus_bullets = surplus_bullets + k - arr[i]
     
    if win:   
        print('YES')
        