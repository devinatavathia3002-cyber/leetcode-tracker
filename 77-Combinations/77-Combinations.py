# Last updated: 4/8/2026, 9:37:13 PM
1class Solution:
2    def combine(self, n: int, k: int) -> List[List[int]]:
3
4        res = []
5        
6        def backtracking(num, subset):
7            nonlocal res
8
9            if len(subset) > k:
10                return
11            
12            if len(subset) == k:
13                res.append(subset.copy())
14            
15            for i in range(num, n + 1):
16                subset.append(i)
17                backtracking(i + 1, subset)
18                subset.pop()
19
20        backtracking(1, [])
21        return res
22