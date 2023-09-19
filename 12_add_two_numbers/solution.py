'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = None
        
        while l1 is not None or l2 is not None:
            l2_val, l1_val = 0, 0
            if l1 is not None:
                l1_val = l1.val
                l1 = l1.next
                
            if l2 is not None:
                l2_val = l2.val
                l2 = l2.next
            
            local_sum = l1_val + l2_val + carry
            
            if local_sum > 9:
                carry = 1
                local_sum -= 10
            else:
                carry = 0
            
            node = ListNode(local_sum)
            if head is None:
                head = node
            else:
                last_node.next = node
                
            last_node = node
        
        if carry != 0:
            last_node.next = ListNode(carry)
        
        return head