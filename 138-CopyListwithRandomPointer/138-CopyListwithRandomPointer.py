# Last updated: 3/9/2026, 11:15:31 PM
1class Solution:
2    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
3
4        randC = {}
5        randO = {}
6
7        dummy = Node(-1)
8
9        p1 = dummy
10        p2 = head
11
12        while p2:
13            node = Node(p2.val)
14            p1.next = node
15
16            randC[node] = p2
17            randO[p2] = node
18
19            p1 = p1.next
20            p2 = p2.next
21
22        p3 = dummy.next
23
24        while p3:
25            original = randC[p3]
26            originalRand = original.random
27
28            if originalRand:
29                p3.random = randO[originalRand]
30
31            p3 = p3.next
32
33        return dummy.next