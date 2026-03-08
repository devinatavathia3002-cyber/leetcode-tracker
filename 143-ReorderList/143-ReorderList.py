# Last updated: 3/7/2026, 5:13:15 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def reorderList(self, head: Optional[ListNode]) -> None:
9        
10        # fast and slow pointer
11        fast = head
12        slow = head
13
14        while fast and fast.next:
15            slow = slow.next
16            fast = fast.next.next
17        
18        p1 = head
19
20        # break link between first and second half of list
21        curr = slow.next
22        slow.next = None
23
24        # reverse second half of list
25        prev = None
26
27        while curr:
28            future = curr.next
29            curr.next = prev
30
31            prev = curr
32            curr = future
33        
34        p2 = prev
35
36        # now we combine
37        curr = p1
38        while p1 and p2:
39            if curr == p1:
40                p1 = p1.next
41                curr.next = p2
42            else:
43                p2 = p2.next
44                curr.next = p1
45            curr = curr.next
46        
47        if p1:
48            curr.next = p1.next
49        if p2:
50            curr.next = p2.next
51        
52        # return nothing