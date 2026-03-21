import sys 

input = sys.stdin.readline

n = int(input())
output = []
for _ in range(n):
    n = int(input())
    s = input().strip()
    
    left, right = 0, n - 1
    turn_count = 0
    cur_turn = 0
    possible = True
    while left < right:
        if s[left] == s[right]:
            if cur_turn == 1:
                turn_count += 1
                cur_turn = 0
        
        else: 
            if cur_turn == 0:
                turn_count += 1
                cur_turn = 1
            
        left += 1
        right -= 1
        
        if turn_count > 2:
            possible = False
            
    if possible:
        output.append('Yes')
    else:
        output.append('No')
        
print('\n'.join(output))