# Last updated: 7/4/2026, 3:33:25 PM
1class Solution:
2    def myAtoi(self, s: str) -> int:
3        res = 0
4        positive = True
5        track = 0
6
7        # pre-processing
8        for i in range(len(s)):
9            curr = s[i]
10            if curr == " ":
11                continue
12            elif curr.isdigit():
13                track = i
14                break
15            elif curr == "-" or curr == "+":
16                if curr == "-":
17                    positive = False
18                track = i + 1
19                break
20            else:
21                return res
22        
23        # process the num
24        while track < len(s) and s[track].isdigit():
25            curr = int(s[track])
26            if curr == 0 and res == 0:
27                track += 1
28                continue
29            res = res * 10
30            res += curr
31
32            track += 1
33
34        if positive == False:
35            res = -1 * res
36        
37        return max(-2**31, min(2**31 - 1, res))