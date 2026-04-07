"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(head: Optional[Node], prev_node: Optional[Node]) -> Optional[Node]:
            if not head:
                return None
            
            head.prev = prev_node
            prev = head
            while head:
                if head.child:
                    next_node = head.next
                    tail = dfs(head.child, head)
                    head.next = head.child
                    head.child = None
                    
                    head = tail
                    head.next = next_node
                    if next_node:
                        next_node.prev = head
                    
                prev = head   
                head = head.next
                
            return prev
        
        dfs(head, None)
        
        return head