# Last updated: 4/7/2026, 8:34:58 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        
4        subs = []
5
6        def backtracking(index, subset):
7            nonlocal subs
8
9            for j in range(index, len(nums)):
10                subset.append(nums[j])
11                backtracking(j + 1, subset)
12                subs.append(subset.copy())
13                subset.pop()
14        
15        backtracking(0, [])
16        subs.append([])
17        return subs