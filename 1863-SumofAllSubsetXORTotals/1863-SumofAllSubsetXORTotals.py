# Last updated: 4/7/2026, 8:18:57 PM
1class Solution:
2    def subsetXORSum(self, nums: List[int]) -> int:
3        
4        # with backtracking
5        res = 0
6
7        def backtracking(index, subset):
8            nonlocal res
9            xOR = 0
10            for num in subset:
11                 xOR ^= num
12            res += xOR
13            
14            for j in range(index, len(nums)):
15                subset.append(nums[j])
16                backtracking(j + 1, subset)
17                subset.pop()
18
19
20        backtracking(0, [])
21        return res