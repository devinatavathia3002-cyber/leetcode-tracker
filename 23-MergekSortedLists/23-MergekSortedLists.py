# Last updated: 3/12/2026, 9:54:06 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:    
8    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
9        
10        if len(lists) < 1:
11            return None
12
13        while len(lists) > 1:
14            merged = []
15            for i in range(0, len(lists), 2):
16                l1 = lists[i]
17                if i < len(lists) - 1:
18                    l2 = lists[i + 1]
19                else:
20                    l2 = None
21                merged.append(self.mergeLists(l1, l2))
22            lists = merged
23        return lists[0]
24
25    def mergeLists(self, l1, l2):
26        dummy = ListNode(-1)
27        tail = dummy
28
29        while l1 and l2:
30            if l1.val < l2.val:
31                tail.next = l1
32                l1 = l1.next
33            else:
34                tail.next = l2
35                l2 = l2.next
36            tail = tail.next
37            
38        if l1:
39            tail.next = l1
40        if l2:
41            tail.next = l2
42
43        return dummy.next