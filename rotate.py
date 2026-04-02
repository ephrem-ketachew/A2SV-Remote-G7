from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        node = head
        n = 0
        while node:
            node = node.next
            n += 1
            
        k %= n
        if k == 0:
            return head
            
        node = head
        for _ in range(n - k - 1):
            node = node.next
            
        new_head = node.next
        node.next = None
        
        node = new_head
        while node.next:
            node = node.next
            
        node.next = head
        
        return new_head