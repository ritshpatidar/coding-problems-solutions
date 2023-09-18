class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next is None or left == right:
            return head
        
        left_start = head
        prev = None
        i = 1
        
        #Find Left
        while i != left:
            prev = left_start
            left_start = left_start.next
            i+=1
        
        # left_start is pointing at node at <left> index
        # Reverse from left to right.
        cur = left_start
        while i>=left and i<=right:
            _next = cur.next
            cur.next = prev
            prev = cur
            cur = _next
            i += 1
        
        # now prev is pointing at last node of reversed part
        # and cur is pointing at right+1 node (whatever is behind)
        if left_start.next is None:
            head = prev
            left_start.next = cur
        else:
            left_start.next.next = prev
            left_start.next = cur
        
        return head