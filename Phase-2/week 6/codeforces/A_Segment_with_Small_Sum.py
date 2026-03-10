# A. Segment with Small Sum
# time limit per test1 second
# memory limit per test1024 megabytes
# Given an array of n
#  integers ai
# . Let's say that the segment of this array a[l..r]
#  (1≤l≤r≤n
# ) is good if the sum of elements on this segment is at most s
# . Your task is to find the longest good segment.

# Input
# The first line contains integers n
#  and s
#  (1≤n≤105
# , 1≤s≤1018
# ). The second line contains integers ai
#  (1≤ai≤109
# ).

# Output
# Print one integer, the length of the longest good segment. If there are no such segments, print 0
# .

# Example
# InputCopy
# 7 20
# 2 6 4 3 6 8 9
# OutputCopy
# 4

n, s = map(int, input().split())

arr = list(map(int, input().split()))

max_len = 0
left = 0
cur_sum = 0
for right in range(len(arr)):
    cur_sum += arr[right]
    while cur_sum > s:
        cur_sum -= arr[left]
        left += 1
        
    max_len = max(max_len, right - left + 1)
    
print(max_len)