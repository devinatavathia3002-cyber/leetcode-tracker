# Last updated: 6/10/2026, 9:05:22 PM
1class Solution:
2    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
3        
4        # subsets with target sum
5        output = []
6        candidates.sort()
7
8        def subsets(i, total, sub):
9            if total == target:
10                output.append(sub.copy())
11                return
12            
13            if total > target:
14                return
15            
16            for j in range(i, len(candidates)):
17                if j > 0 and candidates[j] == candidates[j - 1] and j != i:
18                    continue
19                sub.append(candidates[j])
20                subsets(j + 1, total + candidates[j], sub)
21                sub.pop()
22
23
24        subsets(0, 0, [])
25        return output