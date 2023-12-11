class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        # APPROACH- brute force using string and int conversion
        '''
        num = ""
        while head:
            num += str(head.val)
            head = head.next
        return int(num, 2)
        '''

        # APPROACH - MSB TO LSB
        res = 0
        while head:
            res = res * 2 + head.val
            head = head.next
        
        return res
    

'''
APPROACH-1
traverse each node and append the value into a string
at then end convert that string into integer

APPROACH-2
traverse each digit as if this the whole binary digit, then move to next by * 2 to result and adding the new digit
MSB to LSB
'''