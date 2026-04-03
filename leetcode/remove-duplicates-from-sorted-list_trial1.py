# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('inf'), head)
        prev = dummy
        node = head
        while node:
            if node.val != prev.val:
                prev.next = node
                prev = prev.next
            
            node = node.next
            
        prev.next = None
        
        return dummy.next