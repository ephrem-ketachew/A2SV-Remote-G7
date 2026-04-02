from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = left_head = ListNode()
        right = right_head = ListNode()
        
        node = head
        while node:
            if node.val < x:
                left.next = node
                left = node
            else:
                right.next = node
                right = node
                
            node = node.next

        right.next = None
            
        left.next = right_head.next
        
        return left_head.next