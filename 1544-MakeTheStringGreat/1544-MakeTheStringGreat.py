# Last updated: 7/16/2026, 6:53:17 PM
1class Solution:
2    def makeGood(self, s: str) -> str:
3        stack = []
4
5        for char in s:
6            if stack:
7                top = stack[-1]
8                if (top.islower() and char.isupper() and top == char.lower()) or (top.isupper() and char.islower() and top == char.upper()):
9                    stack.pop()
10                    continue
11            stack.append(char)
12
13        return "".join(stack)
14