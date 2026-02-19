# Last updated: 2/18/2026, 11:13:47 PM
1class Solution:
2    def openLock(self, deadends: List[str], target: str) -> int:
3        
4        # let's try this with standard bfs first
5        visited = set(deadends)
6        q = deque()
7        q.append(("0000", 0))
8
9        # edge case
10        if target in deadends or "0000" in deadends:
11            return -1
12
13        # main loop
14        while q:
15            for j in range(len(q)):
16                val, steps = q.popleft()
17                if val == target:
18                    return steps
19
20                for i in range(4):
21                    digit1 = (int(val[i]) + 1) % 10
22                    val1 = val[:i] + str(digit1) + val[i + 1:]
23
24                    digit2 = (int(val[i]) - 1 + 10) % 10
25                    val2 = val[:i] + str(digit2) + val[i + 1:]
26
27                    if val1 == target or val2 == target:
28                        return steps + 1
29                    if val1 not in visited:
30                        q.append((val1, steps + 1))
31                        visited.add(val1)
32                    if val2 not in visited:
33                        q.append((val2, steps + 1))
34                        visited.add(val2)
35
36        return -1