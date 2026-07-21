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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int c=0;
        ListNode temp=head;
        while(temp!=null){
            c++;
            temp=temp.next;
        }
        ListNode tempo=head;
        if(c==n){
            return head.next;
        }
        else{
            while(c>n+1){
                tempo=tempo.next;
                c--;
            }
            tempo.next=tempo.next.next;
        }
        return head;
        


    }
}
