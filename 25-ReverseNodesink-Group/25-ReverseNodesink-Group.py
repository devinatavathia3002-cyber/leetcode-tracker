# Last updated: 3/12/2026, 11:02:14 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
9        
10        dummy = ListNode(-1)
11        dummy.next = head
12        prevNode = dummy
13
14        while True:
15            start = prevNode.next
16            curr = prevNode
17
18            # find if we have to break or not
19            counter = k
20            print(curr.val)
21            while curr and counter > 0:
22                curr = curr.next
23                counter -= 1
24            if counter > 0 or curr is None:
25                break
26            
27            postNode = curr.next
28
29            #prevNode, start, curr, postNode
30
31            prev = None
32            curr = start
33
34            while curr != postNode:
35                future = curr.next
36                curr.next = prev
37                prev = curr
38                curr = future
39            
40            prevNode.next = prev
41            start.next = postNode
42
43            prevNode = start
44
45        return dummy.next