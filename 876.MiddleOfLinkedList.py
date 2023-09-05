# trick: slow is always half of fast
# kinda similar to 141.Linked List Cycle

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)

def middleNode(self, head: [ListNode]) -> [ListNode]:
    slow, fast = head, head
    
    while slow and fast and fast.next:     
        slow = slow.next
        fast = fast.next.next
    
    return slow

# ll = ListNode(1,2)
# ll = ListNode(2,3)
# print(ll)