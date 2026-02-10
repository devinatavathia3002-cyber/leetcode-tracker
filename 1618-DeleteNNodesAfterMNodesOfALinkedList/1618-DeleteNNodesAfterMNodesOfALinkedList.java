// Last updated: 2/9/2026, 9:53:59 PM
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteNodes(ListNode head, int m, int n) {
        
        if(head == null || (head.next == null && n > 0)) return null;
        if(head.next == null) return head;

        ListNode traversal = head;

        int keep = m;
        int take = n;

        while(traversal != null) {
            while(traversal != null && keep > 1) {
                traversal = traversal.next;
                keep--;
            }

            keep = m;

            while(traversal != null && traversal.next != null && take > 0) {
                traversal.next = traversal.next.next;
                take--;
            }

            if(traversal != null) traversal = traversal.next;
            take = n;
        }

        return head;
    }
}