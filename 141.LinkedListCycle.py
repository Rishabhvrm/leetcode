# FLOYD'S CYCLE-FINDING ALGORITHM
# FLOYD'S hare and tortoise algo (fast and slow pointers)
# faster will catch up slower one eventually
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional [ListNode]) -> bool:
    # using fast and slow pointers (floyd's)
    # T(N) = O(n)
    # Space = O(n)
    if head:
        slow, fast = head, head

        while fast and fast.next:
            # update pointers
            slow = slow.next
            fast = fast.next.next

            # if tortoise and hare are at same place
            # there is a cycle
            if slow == fast: return True

        return False
    
    ## using set
    # T(N) = O(n)
    # Space = O(n)
    visited = set()
    curr = head
    while curr:
        if curr in visited: return True         # found a cycle
        else: visited.add(curr)
        curr = curr.next
    return False