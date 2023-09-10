# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        
        ## BRUTE FORCE - beats 72%, extra space
        ## T(N): O(N)
        ## SPACE COMPLEXITY: O(N), extra array to store reversed order
        ## CONVERT TO ARRAY
        ## REVERESE IT AND COMPARE
        p = head
        arr, rev_arr = [], []
        
        # convert to array
        while p:
            arr.append(p.val)
            p = p.next

        # reverse array
        rev_arr = arr[::-1]

        if arr == rev_arr:
            return True

        