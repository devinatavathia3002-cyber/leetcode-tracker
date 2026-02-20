# Last updated: 2/19/2026, 10:57:49 PM
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        
4        stack = []
5
6        for token in tokens:
7            if token == "+":
8                stack.append(stack.pop() + stack.pop())
9            elif token == "*":
10                stack.append(stack.pop() * stack.pop())
11            elif token == "-":
12                a = stack.pop()
13                b = stack.pop()
14                stack.append(b - a)
15            elif token == "/":
16                a = stack.pop()
17                b = stack.pop()
18                stack.append(int(b / a))
19            else:
20                stack.append(int(token))
21        
22        return stack.pop()