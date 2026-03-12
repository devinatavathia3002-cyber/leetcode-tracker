# Last updated: 3/12/2026, 12:22:51 AM
1class Node:
2    def __init__(self, key, val):
3        self.key = key
4        self.val = val
5        self.next = self.prev = None
6
7class LRUCache:
8    def __init__(self, capacity: int):
9        self.capacity = capacity
10        self.cache = {}
11
12        self.front = Node(0, 0)
13        self.back = Node(0, 0)
14
15        self.front.next = self.back
16        self.back.prev = self.front
17        
18    def insert(self, node):
19        past = self.back.prev
20
21        past.next = node
22        node.prev = past
23
24        self.back.prev = node
25        node.next = self.back
26    
27    def remove(self, node):
28        past = node.prev
29        future = node.next
30
31        past.next = future
32        future.prev = past
33
34    def get(self, key: int) -> int:
35        if key in self.cache:
36            curr = self.cache[key]
37            self.remove(curr)
38            self.insert(curr)
39            return curr.val
40        return -1
41
42    def put(self, key: int, value: int) -> None:
43        newNode = Node(key, value)
44
45        if key in self.cache:
46            curr = self.cache[key]
47            self.remove(curr)
48            self.insert(newNode)
49        else:
50            if len(self.cache) == self.capacity:
51                remVal = self.front.next
52                self.remove(remVal)
53                self.cache.pop(remVal.key)
54            self.insert(newNode)
55        
56        self.cache[key] = newNode