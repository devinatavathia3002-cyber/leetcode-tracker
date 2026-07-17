# Last updated: 7/16/2026, 8:39:07 PM
1class Solution:
2    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
3        stack = []
4
5        i, j = 0, 0
6
7        while j < len(popped):
8            if stack:
9                if stack[-1] != popped[j]:
10                    if i == len(pushed):
11                        return False
12                    stack.append(pushed[i])
13                    i += 1
14                else:
15                    while stack and j < len(popped) and stack[-1] == popped[j]:
16                        stack.pop()
17                        j += 1
18            else:
19                if i == len(pushed):
20                    return False
21                stack.append(pushed[i])
22                i += 1
23        
24        if stack:
25            return False
26        return True
27
28
29