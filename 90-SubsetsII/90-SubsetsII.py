# Last updated: 4/10/2026, 2:59:27 PM
1class Solution:
2    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
3        
4        res = []
5        nums.sort()
6
7        def backtracking(index, sub):
8            nonlocal res
9            res.append(sub.copy())
10
11            for i in range(index, len(nums)):
12                if i > index and nums[i] == nums[i - 1]:
13                    continue
14                sub.append(nums[i])
15                backtracking(i + 1, sub)
16                sub.pop()
17
18        backtracking(0, [])
19        return res