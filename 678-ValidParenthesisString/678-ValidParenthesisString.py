# Last updated: 5/11/2026, 5:56:42 PM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        
4        star = []
5        openS = []
6
7        for i in range(len(s)):
8            char = s[i]
9            if char == ")":
10                if len(openS) > 0:
11                    openS.pop()
12                elif len(star) > 0:
13                    star.pop()
14                else:
15                    return False
16            elif char == "(":
17                openS.append(i)
18            else:
19                star.append(i)
20        
21        if len(openS) > len(star):
22            return False
23            
24        while openS:
25            openIndex = openS.pop()
26            starIndex = star.pop()
27            if starIndex <= openIndex:
28                return False
29
30        return True