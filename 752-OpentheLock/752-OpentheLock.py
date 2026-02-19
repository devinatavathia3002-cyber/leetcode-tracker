# Last updated: 2/18/2026, 11:02:56 PM
1class Solution:
2    def openLock(self, deadends: List[str], target: str) -> int:
3        
4        # let's try this with standard bfs first
5        visited = set(deadends)
6        q = deque()
7        q.append("0000")
8        steps = 0
9
10        # edge case
11        if target in deadends or "0000" in deadends:
12            return -1
13
14        # main loop
15        while q:
16            steps += 1
17            for j in range(len(q)):
18                val = q.popleft()
19                if val == target:
20                    return steps - 1
21
22                for i in range(4):
23                    digit1 = (int(val[i]) + 1) % 10
24                    val1 = val[:i] + str(digit1) + val[i + 1:]
25
26                    digit2 = (int(val[i]) - 1 + 10) % 10
27                    val2 = val[:i] + str(digit2) + val[i + 1:]
28
29                    if val1 == target or val2 == target:
30                        return steps
31                    if val1 not in visited:
32                        q.append(val1)
33                        visited.add(val1)
34                    if val2 not in visited:
35                        q.append(val2)
36                        visited.add(val2)
37
38        return -1