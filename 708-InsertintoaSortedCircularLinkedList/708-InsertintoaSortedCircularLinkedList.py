# Last updated: 8/2/2026, 4:59:32 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val=None, next=None):
5        self.val = val
6        self.next = next
7"""
8
9class Solution:
10    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
11        if not head:
12            head = Node(insertVal)
13            head.next = head
14            return head
15        else:
16            track = head.next
17            prev = head
18
19            while track != head:
20                # normal case
21                if prev.val <= insertVal <= track.val:
22                    break
23                elif prev.val > track.val and (insertVal >= prev.val or insertVal <= track.val):
24                    break
25                else:
26                    prev = track
27                    track = track.next
28            
29
30        newNode = Node(insertVal)
31        prev.next = newNode
32        newNode.next = track
33        return head
34