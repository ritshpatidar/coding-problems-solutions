class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        torto = head.next
        hare = head.next.next
        
        while torto != hare:
            if hare is None or hare.next is None:
                return None
            
            torto = torto.next
            hare = hare.next.next
        
        while torto != head:
            torto = torto.next
            head = head.next
        
        return head