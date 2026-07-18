# Last updated: 7/18/2026, 4:46:43 PM
1class Solution:
2    def addSpaces(self, s: str, spaces: List[int]) -> str:
3        # should be an easy lolz
4        res = [""] * (len(s) + len(spaces))
5        pt = 0
6
7        for i in range(len(s)):
8            if pt < len(spaces) and i == spaces[pt]:
9                res.append(" ")
10                pt += 1
11            res.append(s[i])
12        
13        return "".join(res)