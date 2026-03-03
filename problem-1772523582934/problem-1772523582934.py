# Last updated: 3/2/2026, 11:39:42 PM
1class TimeMap:
2
3    def __init__(self):
4        self.keyStore = {}
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        if key not in self.keyStore:
8            self.keyStore[key] = [[value, timestamp]]
9        else:
10            self.keyStore[key].append([value, timestamp])
11
12    def get(self, key: str, timestamp: int) -> str:
13        
14        if key not in self.keyStore:
15            return ""
16
17        arr = self.keyStore[key]
18        
19        r = len(arr) - 1
20        l = 0
21
22        res = ""
23        while l <= r:
24            m = ((r - l) // 2) + l
25            if arr[m][1] <= timestamp:
26                res = arr[m][0]
27                l = m + 1
28            else:
29                r = m - 1
30        
31        return res