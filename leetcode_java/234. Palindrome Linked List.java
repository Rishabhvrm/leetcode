package leetcode_java;


//  Definition for singly-linked list.
 class ListNode {
     int val;
     ListNode next;
     ListNode() {}
     ListNode(int val) { this.val = val; }
     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }
 

class Solution {

    public static ListNode findMiddle(ListNode node) {
        ListNode fast = node, slow = node;

        // fast will go till last node or till just right of last node
        // while ((fast.next != null) && (fast != null)) { this won't work bcz what if fast is null, you're checking null.next
        while ((fast != null) && (fast.next != null)) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;  // slow will point to the middle
    }

    public static ListNode reverseLL(ListNode node) {
        ListNode prev = null, curr = node, nxt = null;

        while (curr != null){
            nxt = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nxt;
        }
        return prev;    // prev will now point to the start of reversed list (end)

    }


    public boolean isPalindrome(ListNode head) {
        // find middle using fast and slow
        ListNode middle = findMiddle(head);

        // reverse the second half
        ListNode tail = reverseLL(middle);

        // check palindrome
        ListNode start = head, end = tail;
        while (end != null) {
            if (start.val != end.val) {
                return false;
            }
            start = start.next;
            end = end.next;
        }
        return true;
        
    }
}