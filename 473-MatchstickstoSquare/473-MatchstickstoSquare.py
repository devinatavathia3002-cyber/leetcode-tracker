# Last updated: 6/14/2026, 4:49:08 PM
1class Solution:
2    def makesquare(self, matchsticks: List[int]) -> bool:
3        arr = [[] for _ in range(4)]
4
5        total = sum(matchsticks)
6        sideLen = total // 4
7
8        if total % 4 != 0:
9            return False
10
11        matchsticks.sort(reverse = True)
12        def backtrack(i):
13            if i == len(matchsticks):
14                return True
15            
16            for j in range(4):
17                if sum(arr[j]) + matchsticks[i] > sideLen:
18                    continue
19                arr[j].append(matchsticks[i])
20                if backtrack(i + 1):
21                    return True
22                arr[j].pop()
23            
24            return False
25        
26        return backtrack(0)