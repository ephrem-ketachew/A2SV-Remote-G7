# A. The Fallen Champion
# time limit per test1 second
# memory limit per test256 megabytes

# In the ancient days of the Seven Kingdoms, when honor and steel decided the fate of men, justice was not always served in courts. Sometimes, it was decided by combat — a tradition known as Trial by Combat, where it was believed that the gods themselves would decide the fate of the accused.

# When a man was accused, he could call for a champion to fight in his place. If the champion claimed victory, the accused would be declared innocent. If the champion fell... the accused would be judged guilty forever.

# Among the warriors of the realm, one name is famed across the lands of G7C — Youssef Hany, one of the finest fighters the kingdom has ever known. A champion who has closed countless battles and stood victorious in the arena time and time again... yet, like all warriors, his victories have not always been consistent.

# Now, a member of the kingdom of G7C stands accused, and once again, Youssef Hany steps forward to fight on behalf of his people.

# Warriors from across the realm gather in the arena. Each warrior is described by:

# the number of combats they have won, and
# the total time they needed to finish their combats.
# You are given the number of combats Youssef Hany has won and the total time he needed, and you are also given n
#  warriors, each with their number of combats won and total time needed.

# A warrior is considered better than another if:

# they have more wins, or
# they have the same number of wins but less total time.
# If Youssef Hany stands as the best warrior in the arena, he will win in the Trial by Combat and save the accused from judgment. Otherwise, he will fall in battle, becoming the Fallen Champion, and the accused shall face their fate.

# Determine the fate of the trial.

# Input
# The first line contains two integers w
#  and t
#  (1≤w,t≤109)
#  — the number of combats won by Youssef Hany and the total time he needed.

# The second line contains an integer n
#  (1≤n≤105)
#  — the number of warriors.

# Each of the next n
#  lines contains two integers wi
#  and ti
#  (1≤wi,ti≤109)
#  — the number of combats won and the total time needed for the i
# -th warrior.

# Output
# Print "The Champion Saves the Accused" if Youssef Hany is the best warrior in the arena; otherwise, print "The Fallen Champion". The output is case-sensitive.

# Examples
# InputCopy
# 5 100
# 5
# 5 100
# 4 99
# 5 99
# 3 120
# 2 21
# OutputCopy
# The Fallen Champion
# InputCopy
# 5 100
# 5
# 5 100
# 4 99
# 5 101
# 3 120
# 2 21
# OutputCopy
# The Champion Saves the Accused

import sys

input = sys.stdin.readline

w, t = map(int, input().split())

n = int(input())

win = True

for _ in range(n):
    wi, ti = map(int, input().split())
    if (wi > w) or (wi == w and ti < t):
        win = False
        
if win:
    print("The Champion Saves the Accused")
else:
    print("The Fallen Champion")