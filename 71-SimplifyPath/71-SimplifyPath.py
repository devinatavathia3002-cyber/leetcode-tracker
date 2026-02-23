# Last updated: 2/22/2026, 4:59:34 PM
1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        
4        # split by backslash
5        paths = path.split("/")
6
7        stack = []
8
9        for c in paths:
10            if c == "..":
11                if stack:
12                    stack.pop()
13            elif c != "" and c != ".":
14                stack.append(c)
15
16        return "/" + "/".join(stack)