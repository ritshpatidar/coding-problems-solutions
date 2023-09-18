class Solution:
    #Remove Data Types If Needed to Run on Local
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        
        while cur is not None:
            if cur.child is not None:
                childCur = cur.child
                while childCur.next is not None:
                    childCur = childCur.next
                curNext = cur.next
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None
                childCur.next = curNext
                if curNext is not None:
                    curNext.prev = childCur
            
            cur = cur.next
        
        return head