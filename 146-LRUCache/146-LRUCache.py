# Last updated: 7/4/2026, 2:21:04 PM
1class ListNode:
2    def __init__(self, key, value):
3        self.key, self.value = key, value
4        self.prev, self.next = None, None
5
6class LRUCache:
7
8    def __init__(self, capacity: int):
9        self.capacity = capacity
10        self.cache = {}
11
12        self.MRU, self.LRU = ListNode(0, 0), ListNode(0, 0)
13        # front is LRU, back is MRU
14        self.MRU.prev, self.LRU.next = self.LRU, self.MRU
15    
16    def delete(self, key):
17        node = self.cache[key]
18        prev, after = node.prev, node.next
19        prev.next, after.prev = after, prev
20    
21    def insert(self, key):
22        # inserting at the back
23        node = self.cache[key]
24        prev, after = self.MRU.prev, self.MRU
25
26        prev.next, after.prev = node, node
27        node.next, node.prev = after, prev
28
29    def get(self, key: int) -> int:
30        if key in self.cache:
31            self.delete(key)
32            self.insert(key)
33            return self.cache[key].value
34        else:
35            return -1
36
37    def put(self, key: int, value: int) -> None:
38        if key in self.cache:
39            self.cache[key].value = value
40            self.delete(key)
41            self.insert(key)
42        else:
43            self.cache[key] = ListNode(key, value)
44            self.insert(key)
45            
46        # reassign capacity if needed
47        if len(self.cache) > self.capacity:
48            mapKey = self.LRU.next.key
49            self.delete(mapKey)
50            del self.cache[mapKey]
51
52