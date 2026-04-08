# Last updated: 4/8/2026, 12:37:59 AM
1class Solution:
2    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
3        
4        res = []
5        candidates.sort()
6
7        def backtracking(index, subset, total):
8            nonlocal res
9
10            if total == target:
11                res.append(subset.copy())
12                return
13
14            if total > target:
15                return
16
17            for i in range(index, len(candidates)):
18                if i > index and candidates[i] == candidates[i - 1]:
19                    continue
20                subset.append(candidates[i])
21                backtracking(i + 1, subset, total + candidates[i])
22                subset.pop()
23
24        backtracking(0, [], 0)
25        return res