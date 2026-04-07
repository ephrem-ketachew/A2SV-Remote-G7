# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
            
        ans = []
        parts_length = length // k
        more = length - parts_length * k
        node = head
        while k > 0:
            cur_head = prev = node
            cur_len = parts_length + (1 if more > 0 else 0)
            for _ in range(cur_len):
                if not node:
                    break
                prev = node
                node = node.next
              
            if prev:  
                prev.next = None
            ans.append(cur_head)
            
            k -= 1
            more = max(0, more - 1)
            
        return ans