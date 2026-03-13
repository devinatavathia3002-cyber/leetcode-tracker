# Last updated: 3/13/2026, 12:51:01 AM
1class Node:
2    def __init__(self, val):
3        self.val = val
4        self.next = None
5        self.prev = None
6
7class MyCircularQueue:
8
9    def __init__(self, k: int):
10        self.capacity = k
11        self.head = Node(-1)
12        self.tail = Node(-1)
13
14        self.head.next = self.tail
15        self.tail.prev = self.head
16        
17
18    def enQueue(self, value: int) -> bool:
19        if self.isFull():
20            return False
21
22        newNode = Node(value)
23        prevNode = self.tail.prev
24
25        prevNode.next = newNode
26        newNode.prev = prevNode
27
28        newNode.next = self.tail
29        self.tail.prev = newNode
30
31        self.capacity -= 1
32        return True
33
34    def deQueue(self) -> bool:
35        if self.head.next == self.tail:
36            return False
37        postNode = self.head.next.next
38        self.head.next = postNode
39        postNode.prev = self.head
40
41        self.capacity +=1
42        return True
43
44    def Front(self) -> int:
45        if self.head.next == self.tail:
46            return -1
47        return self.head.next.val
48
49    def Rear(self) -> int:
50        if self.tail.prev == self.head:
51            return -1
52        return self.tail.prev.val
53
54    def isEmpty(self) -> bool:
55        if self.tail.prev == self.head:
56            return True
57        return False
58
59    def isFull(self) -> bool:
60        if self.capacity == 0:
61            return True
62        return False
63
64
65# Your MyCircularQueue object will be instantiated and called as such:
66# obj = MyCircularQueue(k)
67# param_1 = obj.enQueue(value)
68# param_2 = obj.deQueue()
69# param_3 = obj.Front()
70# param_4 = obj.Rear()
71# param_5 = obj.isEmpty()
72# param_6 = obj.isFull()