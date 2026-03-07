# Last updated: 3/7/2026, 2:20:57 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
9        
10        dummy = ListNode(0)
11        curr = dummy
12
13        p1 = list1
14        p2 = list2
15
16        while p1 and p2:
17            if p1.val < p2.val:
18                curr.next = p1
19                p1 = p1.next
20            else:
21                curr.next = p2
22                p2 = p2.next
23            curr = curr.next
24        
25        if p1:
26            curr.next = p1
27        if p2:
28            curr.next = p2
29
30        return dummy.next