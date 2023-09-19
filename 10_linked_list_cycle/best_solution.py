#Torto goes 1 step at a time, and hare goes 2 steps at a time
#If cycle is there, they will meet eventually
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        
        torto = head.next
        hare = head.next.next
        
        while torto != hare:
            if hare is None or hare.next is None:
                return False
            
            torto = torto.next
            hare = hare.next.next
        
        return True