# Last updated: 7/14/2026, 11:52:12 PM
1class Solution:
2    def minOperations(self, logs: List[str]) -> int:
3        stack = []
4
5        for log in logs:
6            if log == "./":
7                continue
8            elif log == "../":
9                if len(stack) > 0:
10                    stack.pop()
11            else:
12                stack.append(log)
13        
14        return len(stack)