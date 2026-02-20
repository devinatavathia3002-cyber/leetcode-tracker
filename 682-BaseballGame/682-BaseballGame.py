# Last updated: 2/19/2026, 10:29:36 PM
1class Solution:
2    def calPoints(self, operations: List[str]) -> int:
3        
4        stack = []
5
6        for i in range(len(operations)):
7            if operations[i] == "D":
8                val = (2 * stack[-1])
9                stack.append(val)
10            elif operations[i] == "+":
11                val = (stack[-1] + stack[-2])
12                stack.append(val)
13            elif operations[i] == "C":
14                stack.pop()
15            else:
16                stack.append(int(operations[i]))
17
18        return sum(stack)