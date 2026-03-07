# Last updated: 3/7/2026, 1:35:23 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
9
10        curr = head
11        prev = None
12
13        while curr:
14            future = curr.next
15            curr.next = prev
16
17            prev = curr
18            curr = future
19        
20        return prev