# Last updated: 3/15/2026, 2:27:50 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
8        
9        dummy = ListNode(-1)
10        dummy.next = head
11
12        prev = dummy
13        curr = head
14
15        remaining = left
16
17        while remaining > 1:
18            prev = curr
19            curr = curr.next
20            remaining -= 1
21        
22        remaining = (right - left)
23        start = curr
24
25        while remaining > 0:
26            curr = curr.next 
27            remaining -= 1
28        
29        end = curr
30        post = curr.next
31
32        # prev and post will connect to to our reversed list in the end
33        dummy = None
34        curr = start
35
36        while curr != post:
37            future = curr.next
38            curr.next = dummy
39            dummy = curr
40            curr = future
41        
42        if prev:
43            prev.next = end
44        start.next = post
45
46        if left == 1:
47            return end
48        return head
49
50
51