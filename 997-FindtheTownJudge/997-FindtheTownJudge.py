# Last updated: 4/14/2026, 8:21:57 PM
1class Solution:
2    def findJudge(self, n: int, trust: List[List[int]]) -> int:
3        
4        # incoming - outgoing array
5        delta = [0] * n
6
7        for sub in trust:
8            per, trusts = sub
9            delta[per - 1] -= 1
10            delta[trusts - 1] += 1
11        
12        for i, num in enumerate(delta):
13            if num == (n - 1):
14                return i + 1
15
16        return -1