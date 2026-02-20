# Last updated: 2/19/2026, 8:30:56 PM
1class Solution:
2    def openLock(self, deadends: List[str], target: str) -> int:
3        
4        visited = set(deadends)
5
6        beg = {"0000"}
7        end = {target}
8
9        steps = 0
10
11        if target in visited or "0000" in visited:
12            return -1
13        
14        if target == "0000":
15            return 0
16
17        while beg and end:
18            if len(beg) > len(end):
19                beg, end = end, beg
20            
21            temp = set()
22            steps += 1
23
24            for lock in beg:
25                
26                for j in range(4):
27                    newVal1 = lock[:j] + str((int(lock[j]) + 1) % 10) + lock[j + 1:]
28                    newVal2 = lock[:j] + str((int(lock[j]) - 1 + 10) % 10) + lock[j + 1:]
29
30                    if newVal1 in end or newVal2 in end:
31                        return steps
32                    
33                    if newVal1 not in visited:
34                        visited.add(newVal1)
35                        temp.add(newVal1)
36                    
37                    if newVal2 not in visited:
38                        visited.add(newVal2)
39                        temp.add(newVal2)
40
41            beg = temp
42
43        return -1