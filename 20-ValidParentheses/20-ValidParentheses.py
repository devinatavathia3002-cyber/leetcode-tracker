# Last updated: 2/19/2026, 12:41:25 AM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        
4        if len(s) % 2 != 0:
5            return False
6
7        stack = []
8        chars = {")" : "(", "]" : "[", "}" : "{"}
9
10        for i in range(len(s)):
11            if s[i] not in chars:
12                stack.append(s[i])
13            else:
14                if stack:
15                    popped = stack.pop()
16                    if popped != chars.get(s[i]):
17                        return False
18                else:
19                    return False
20        
21        if stack:
22            return False
23        return True