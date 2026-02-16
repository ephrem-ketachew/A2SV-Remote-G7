# C. Eternal Timers
# time limit per test1.5 s.
# memory limit per test512 MB
# You are given a sequence of n
#  mechanical timers arranged in a straight line. The initial value displayed on the i
# -th timer is ai
# .

# Every second, the following events occur in order:

# The value on each timer decreases by 1
# . If the value of any timer becomes 0
# , you immediately lose.
# You may move to an adjacent timer (to the left or right) or remain at your current timer.
# You may reset the timer you are currently standing on back to its original value ai
# .
# Note that these events happen strictly in the given order. If the value of a timer becomes 0
#  during the first step of a second, you lose instantly, even if you could move to that timer and reset it later during the same second.

# You may start at any timer. Determine whether it is possible to continue this process indefinitely without losing.

# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.

# For each test case, the first line contains a single integer n
#  (2≤n≤5⋅105
# ) — the number of timers.

# The second line contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ) — the initial values of the timers.

# It is guaranteed that the sum of n
#  over all test cases does not exceed 5⋅105
# .

# Output
# For each test case, print "YES" (without quotes) if it is possible to continue the process indefinitely, or "NO" (without quotes) otherwise.

# You may print "YES" and "NO" in any letter case (for example, "yEs", "yes", and "Yes" will all be accepted as correct).

# Example
# InputCopy
# 5
# 2
# 4 10
# 2
# 2 2
# 3
# 4 10 5
# 3
# 5 3 5
# 5
# 12 13 25 17 30
# OutputCopy
# YES
# NO
# NO
# YES
# YES
# Note
# In the first test case, you can repeatedly move back and forth between the two timers, resetting them in turn.

# In the third test case, suppose you start at timer 1
#  and follow the strategy below:

# Initially, a=[4,10,5]
# .

# a
#  becomes [3,9,4]
# . You move to timer 2
#  and reset it, resulting in a=[3,10,4]
# .
# a
#  becomes [2,9,3]
# . You move to timer 3
#  and reset it, resulting in a=[2,9,5]
# .
# a
#  becomes [1,8,4]
# . You move to timer 2
#  and reset it, resulting in a=[1,10,4]
# .
# a
#  becomes [0,9,3]
# . You attempt to move to timer 1
# , but you lose because a1
#  has reached 0
# .
# It can be proven that no possible strategy allows you to continue indefinitely.



t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    can_win = True
    for i in range(len(arr)):
        max_len = 2 * max(i, n - i - 1)
        if arr[i] <= max_len:
            can_win = False
            break
        
    if can_win:
        print('YES')
    else:
        print('NO')
    