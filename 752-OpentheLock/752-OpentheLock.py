# Last updated: 4/16/2026, 10:10:53 PM
1class Solution:
2    def openLock(self, deadends: List[str], target: str) -> int:
3        
4        if "0000" in deadends:
5            return -1
6            
7        visited = set()
8        for num in deadends:
9            visited.add(num)
10        
11        q = deque()
12        q.append("0000")
13        visited.add("0000")
14
15        output = 0
16
17        while q:
18            length = len(q)
19            for i in range(length):
20                popped = q.popleft()
21                if popped == target:
22                    return output
23
24                for j in range(4):
25                    pos = (int(popped[j]) + 1) % 10
26                    minus = (int(popped[j]) - 1) % 10
27                    down = popped[:j] + str(minus) + popped[j + 1:]
28                    up = popped[:j] + str(pos) + popped[j + 1:]
29                    if up not in visited:
30                        q.append(up)
31                        visited.add(up)
32                    if down not in visited:
33                        q.append(down)
34                        visited.add(down)
35            output += 1
36
37        return -1