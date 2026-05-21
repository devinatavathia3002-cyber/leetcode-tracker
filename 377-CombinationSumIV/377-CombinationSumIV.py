# Last updated: 5/20/2026, 10:59:10 PM
1class Solution:
2    def combinationSum4(self, nums: List[int], target: int) -> int:
3        nums.sort()
4        dp = {}
5
6        def recurse(total):
7            if total in dp:
8                return dp[total]
9            if total == target:
10                return 1
11            if total > target:
12                return 0
13            
14            dp[total] = 0
15            for i in range(len(nums)):
16                dp[total] += recurse(nums[i] + total)
17            
18            return dp[total]
19
20        return recurse(0)