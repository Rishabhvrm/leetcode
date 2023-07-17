# FLOYD'S CYCLE-FINDING ALGORITHM
# FLOYD'S hare and tortoise algo (fast and slow pointers)

def hasCycle(head: Optional [ListNode]) -> bool:
    if head:
        slow, fast = head.next, head.next

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # if tortoise and hare are at same place
            # there is a cycle
            if slow == fast:
                return True

        return False