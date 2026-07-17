# Last updated: 7/16/2026, 7:12:04 PM
1class Solution:
2    def removeStars(self, s: str) -> str:
3        stack = []
4
5        for char in s:
6            if char == "*":
7                stack.pop()
8                continue
9            else:
10                stack.append(char)
11        
12        return "".join(stack)