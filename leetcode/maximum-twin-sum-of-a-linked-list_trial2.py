# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node = head
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
          
        max_sum = 0  
        left, right = 0, len(arr) - 1
        while left < right:
            max_sum = max(max_sum, arr[left] + arr[right])
            left += 1
            right -= 1
            
        return max_sum