# Last updated: 4/7/2026, 11:11:05 PM
1class Solution:
2    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
3        
4        res = []
5
6        def backtracking(index, subset, total):
7            nonlocal res
8
9            if total == target:
10                res.append(subset.copy())
11                return
12            if total > target:
13                return
14
15            for i in range(index, len(nums)):
16                subset.append(nums[i])
17                backtracking(i, subset, total + nums[i])
18                subset.pop()
19
20        backtracking(0, [], 0)
21        return res