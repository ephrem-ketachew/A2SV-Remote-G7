import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    d = list(map(int, input().split()))

    d_h = [(deadline, health) for deadline, health in zip(d, h)]
    d_h.sort()

    def can_defeat(x: int) -> bool:
        cur_time = 0
        for deadline, health in d_h:
            time = (health + x - 1) // x
            cur_time += time
            if cur_time > deadline:
                return False
            
        return True

    low, high = 1, max(h)
    ans = float('inf')
    while low <= high:
        mid = (low + high) // 2
        if can_defeat(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)