# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:   
        prev = dummy_head = ListNode(0, head)
        node = head
        while node and node.next:
            next_node = node.next
            third_node = next_node.next

            node.next = third_node
            next_node.next = node
            prev.next = next_node
            
            prev = node
            node = third_node
            
        return dummy_head.next