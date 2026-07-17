# Last updated: 7/16/2026, 10:12:18 PM
1class Solution:
2    def removeKdigits(self, num: str, k: int) -> str:
3        stack = []
4        count = k
5
6        for val in num:
7            while stack and count > 0 and stack[-1] > val:
8                stack.pop()
9                count -= 1
10            stack.append(val)
11
12        output = "".join(stack)
13        if count > 0:
14            output = output[:-count]
15        while output and output[0] == "0":
16            output = output[1:]
17        if output:
18            return output 
19        else:
20            return "0"