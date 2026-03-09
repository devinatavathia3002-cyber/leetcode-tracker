# Last updated: 3/8/2026, 7:38:39 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
9        
10        dummy = ListNode(-1)
11        dummy.next = head
12
13        start = head
14        behind = dummy
15
16        while n:
17            start = start.next
18            n -= 1
19        
20        while start:
21            behind = behind.next
22            start = start.next
23        
24        if behind.next == head:
25            return head.next
26
27        behind.next = behind.next.next
28        return head