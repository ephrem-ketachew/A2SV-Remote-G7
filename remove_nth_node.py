from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        i = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            i += 1
            
        length = 2 * i + (1 if fast else 0)
        index = length - n + 1
        
        if index <= length // 2 + 1:
            prev = dummy_node = ListNode()
            dummy_node.next = head
            cur = head
            i = 1
            while i < index:
                prev = cur
                cur = cur.next
                i += 1
                
            prev.next = cur.next
            
            return dummy_node.next
        
        else:
            index = index - length // 2
            cur = slow
            i = 1
            while i < index:
                prev = cur
                cur = cur.next
                i += 1
                
            prev.next = cur.next
            
            return head
                