t = int(input())

for _ in range(t):
    n, p = map(int, input().split())
    residents = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    
    cost_resident = sorted(zip(cost, residents))
    
    min_cost = p
    count = 1
    i = 0
    while count < n and i < n:
        cur_cost, cur_res = cost_resident[i]
        if cur_cost < p:
            needed = min(n - count, cur_res)
            min_cost += needed * cur_cost
            count += needed
        else:
            min_cost += (n - count) * p
            count = n
            break
        
        i += 1
        
    if count < n:
        min_cost += (n - count) * p
        
    print(min_cost)