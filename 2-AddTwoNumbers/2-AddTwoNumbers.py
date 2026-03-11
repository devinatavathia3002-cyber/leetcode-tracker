# Last updated: 3/10/2026, 8:42:19 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
9        
10        p1 = l1
11        p2 = l2
12
13        carry = 0
14        
15        dummy = ListNode(-1)
16        head = dummy
17
18        while l1 or l2:
19            if l1 and l2:
20                total = l1.val + l2.val + carry
21            elif l1:
22                total = l1.val + carry
23            else:
24                total = l2.val + carry
25
26            newVal = total % 10
27
28            head.next = ListNode(newVal)
29            head = head.next
30
31            carry = total // 10
32            print(carry)
33
34            if l1:
35                l1 = l1.next
36            if l2:
37                l2 = l2.next
38        
39        if carry > 0:
40            head.next = ListNode(carry)
41            head = head.next
42
43        return dummy.next