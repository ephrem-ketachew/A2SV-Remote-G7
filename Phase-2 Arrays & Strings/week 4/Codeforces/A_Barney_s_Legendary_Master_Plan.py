# A. Barney’s Legendary Master Plan
# time limit per test1 s.
# memory limit per test1024 MB
# Bro.

# Barney Stinson starts with nothing. Zero. An array a
#  of size n
# , filled with zeros.

# But Barney doesn’t do “zero.” He does legendary.

# His mission is to transform this boring zero-array into a specific target lifestyle (the given array) using the minimum number of moves.

# And as always, Barney has exactly two plays in his Playbook™:

# Suit Up (Increase): Barney picks a positive integer x
#  and adds it to every single element in the array.
# Because when Barney levels up… he levels everything up.

# Formally, for each i
#  (1≤i≤n
# ), he replaces ai
#  with ai+x
# .

# Total commitment. No half-measures.


# The Reset Bro (Smash): Sometimes a move isn’t working.
# Barney can choose any elements (maybe none, maybe all) and reset them to 0
# .

# For each i
#  (1≤i≤n
# ), he either keeps ai
#  as it is or replaces it with 0
# .

# Keep it. Or wipe it out completely.

# New identity. New plan. New legendary opportunity.

# Given the final legendary target array, determine the minimum number of total plays (Suit Up and Reset Bro) Barney needs to execute.

# And trust me, Ted… no matter the target, there’s always a way to make it legendary.

# It can be shown that for any given final array, a sequence of operations always exists.

# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤1000
# ). The description of the test cases follows.

# The first line contains a single integer n
#  (1≤n≤100
# ) — the number of elements in the array a
# .

# The second line contains n
#  integers a1,a2,…,an
#  (1≤ai≤100
# ) — the elements of the target lifestyle.

# Output
# For each test case, output a single integer — the minimum number of legendary plays required.

# Example
# InputCopy
# 3
# 3
# 1 1 3
# 1
# 100
# 9
# 9 9 3 2 4 4 8 5 3
# OutputCopy
# 3
# 1
# 11
# Note
# Explanation of the first test case:

# The target lifestyle is [1,1,3]
# . A possible sequence of 3
#  plays (which is the minimum) is:

# Initially, the array is [0,0,0]
# . After a Suit Up play with x=2
# , the array becomes [2,2,2]
# .
# Next, after a Reset Bro play on the first two elements, the array becomes [0,0,2]
# .
# Finally, after a Suit Up play with x=1
# , the array becomes [1,1,3]
# .
# We used 2
#  Suit Up plays and 1
#  Reset Bro play for a total of 3
#  plays.

# Explanation of the second test case:

# The target lifestyle is [100]
# . A single Suit Up play with x=100
#  gives the target lifestyle.

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = len(set(arr))
    print(2 * m - 1)