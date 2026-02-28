# Last updated: 2/27/2026, 6:25:07 PM
1class Solution:
2    def decodeString(self, s: str) -> str:
3        
4        stack = []
5
6        for i in range(len(s)):
7            if s[i] != "]":
8                stack.append(s[i])
9            else:
10                output = ""
11                while stack[-1] != "[":
12                    output = stack.pop() + output
13                
14                stack.pop()
15                digit = ""
16                while stack and stack[-1].isdigit():
17                    digit = stack.pop() + digit
18                
19                stack.append(int(digit) * output)
20
21
22        return "".join(stack)