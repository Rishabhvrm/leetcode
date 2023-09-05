# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # create dummy node
        head = ListNode()
        current = head

        while list1 and list2:
            # if ele in list1 < ele in list2
            # point the current list to list1
            # update the list1 pointer to next val
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            # if ele in list1 > ele in list2
            # point the current list to list2
            # update the list2 pointer to next val
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # if any of the lists ends (i.e one is smaller than the other)
        current.next = list1 or list2
        
        # dummy node is empty
        # return the next of dummy node which has the whole list
        return head.next
        