# E. Jon Snow’s Great Escape
# time limit per test1 s.
# memory limit per test256 MB

# In the ancient days of the Seven Kingdoms, far beyond the Wall where the cold winds howl, creatures of ice and darkness roam the frozen lands.

# The Night King raises walls of ice to trap the living, and few who enter ever return.

# Now, Jon Snow stands alone in this icy wasteland, with only Longclaw and his wits to guide him toward freedom.

# Jon Snow is trapped in a 1×n
#  icy canyon. Some cells have Ice Walls (#), others are empty (.). Jon starts at an empty cell x
# .

# The Night King wants to keep Jon trapped as long as possible. Jon wants to escape immediately.

# In each day, the following events happen in order:

# The Night King builds one Ice Wall in any empty cell (except where Jon is).
# Jon chooses a direction: Left or Right.
# If there are no Ice Walls in the chosen direction, Jon escapes the canyon immediately, and the trial ends.
# If there are Ice Walls in that direction, Jon charges the nearest one, shatters it with Longclaw, and takes its place. He ends the day standing in the cell where the wall used to be.
# Here is an example of a possible sequence of actions when n=6
#  and x=4
# :


# Jon is a master tactician and knows exactly where all walls are at all times. He plays to minimize the number of days to escape, while the Night King plays to maximize them.

# Given the initial state of the canyon, determine the number of days Jon will take to escape if both play optimally.

# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.

# The first line of each test case contains two integers n
#  and x
#  (2≤n≤2⋅105
# , 1≤x≤n
# ) — the size of the grid and the initial position of Jon Snow.

# The second line contains a string s
#  of length n
#  (si="#"
#  or "."
# ) — the initial state of the grid. The i
# -th cell of the grid contains a ice wall if si="#"
# , and it is empty if si="."
# .

# It is guaranteed that the x
# -th cell is empty, and there are at least two empty cells in the grid.

# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .

# Output
# For each test case, output a single integer — the number of days Jon Snow needs to escape the grid if they both act optimally.

# Example
# InputCopy
# 4
# 3 1
# ..#
# 4 2
# ....
# 5 3
# ##..#
# 6 4
# #...#.
# OutputCopy
# 1
# 1
# 3
# 3
# Note
# In the first test case, Night King must build an ice wall in cell 2
# , so Jon can escape from the left side of the grid on the first day.

# In the second test case, if Night King places the ice wall to the left of Jon, Jon can escape from the right. And if the ice wall is to Jon's right, he can escape from the left. Thus, the answer is 1
# .

# In the third test case:

# It can be shown that both players acted optimally in the above illustration.

# In the fourth test case, The example image provided in the problem statement illustrates how the game is played. It shows the sequence of building and destroying walls. However, please note that the players in this specific image did not act optimally. It is used only to demonstrate the movement mechanics. In your solution, you must assume both Jon and the Night King play perfectly to achieve their goals.

import sys

input = sys.stdin.readline

t = int(input())

output = []
for _ in range(t):
    n, x = map(int, input().split())
    
    s = input().strip()
    
    left_walls = s[:x-1].count('#')
    right_walls = s[x:].count('#')
    
    if left_walls == 0 and right_walls == 0:
        ans = 1
        
    elif left_walls > 0 and right_walls > 0:
        right_escape_idx = x + s[x:].find('#') + 1
        left_escape_idx = s[:x-1].rfind('#') + 1
        ans = max(min(x, n - right_escape_idx + 2), min(left_escape_idx + 1, n - x + 1))
        
    elif left_walls == 0 and right_walls > 0:
        right_escape_idx = x + s[x:].find('#') + 1
        ans = min(x, n - right_escape_idx + 2)
        
    else:
        left_escape_idx = s[:x-1].rfind('#') + 1
        ans = min(left_escape_idx + 1, n - x + 1)
        
    output.append(str(ans))
    
    
print('\n'.join(output))