from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:
            return head
        
        dummy = ListNode()
        dummy.next = head
        
        prev = None
        cur = dummy
        i = 0
        while i < left:
            prev = cur
            cur = cur.next
            i += 1
            
        left_end = prev
        while i <= right:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            i += 1
        
        left_end.next.next = cur
        left_end.next = prev
            
        return dummy.next