# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # contains only 1 element
        if head.next is None:
            return None
        
        # contains more than 1 element
        count = 0
        behind, ahead = head, head

        # make ahead and behind n distance units apart
        # by moving only 'ahead'
        for _ in range(n):
            ahead = ahead.next

        # if ahead reaches \0
        # means n is equal to the length of LL
        # meaning skip first element
        if ahead is None:
            return head.next        # skip first element

        # till reached end of list
        # ahead will start from n distance apart to behind
        while(ahead.next):

            # ahead and behind are now n distance units apart
            # traverse till the end of the list
            # when ahead will point to end of list
            # behind will be just behind the target element
            ahead = ahead.next
            behind = behind.next


        # make behind point the next of target
        # hence skip target
        behind.next = behind.next.next
        return head