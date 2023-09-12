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
        
        arr = []
        
        # convert to array
        while head:
            arr.append(head.val)
            head = head.next

        # reverse array
        # rev_arr = []
        # rev_arr = arr[::-1]

        l, r = 0, len(arr) -1
        while l <= r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1

        return True

        # if arr == rev_arr:
        #     return True
        
    def isPalindrome2(self, head) -> bool:
        
        # T(N) = O(N)
        # SPACE - O(1)

        # FIND MIDDLE TO
        # REVERSE SECOND HALF 
        # POINT TO FIRST AND LAST AND CHECK FOR PALINDROME

        # find middle using floyd's cycle detection algorithm
        # also finds middle if no cycle (fast and slow pointers)
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev = None
        while slow:                         # slow points to null
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
    
        # second half of LL is reversed
        # check palindrome
        left, right = head, prev
        while right:                        # until right reaches the middle i.e. None
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

        