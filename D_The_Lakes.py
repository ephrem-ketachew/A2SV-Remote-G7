import sys 
from collections import deque

input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 4)

t = int(input())
output = []
for _ in range(t):
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
        
    # def dfs(r: int, c: int) -> int:
    #     if r == -1 or r == n or c == -1 or c == m or grid[r][c] == 0:
    #         return 0
        
    #     count = grid[r][c]
    #     grid[r][c] = 0
        
    #     count += dfs(r - 1, c)
    #     count += dfs(r + 1, c)
    #     count += dfs(r, c + 1)
    #     count += dfs(r, c - 1)
        
    #     return count
    
    queue = deque([])
    
    max_vol = 0
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                # max_vol = max(max_vol, dfs(i, j))
                queue = deque([(i, j)])
                count = grid[i][j]
                grid[i][j] = 0
                while queue:
                    x, y = queue.popleft()
                    for dr, dc in moves:
                        r, c = x + dr, y + dc
                        if 0 <= r < n and 0 <= c < m and grid[r][c] != 0:
                            count += grid[r][c]
                            queue.append((r, c))
                            grid[r][c] = 0
                            
                max_vol = max(max_vol, count)
                
    output.append(str(max_vol))
    
print('\n'.join(output))