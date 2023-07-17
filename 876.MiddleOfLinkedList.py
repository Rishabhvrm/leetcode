# trick: slow is always half of fast
# kinda similar to 141.Linked List Cycle

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head
    
    while slow and fast and fast.next:     
        slow = slow.next
        fast = fast.next.next
    
    return slow