# Last updated: 5/20/2026, 7:48:54 PM
1class Solution:
2    def maxCoins(self, nums: List[int]) -> int:
3        
4         dp = {}
5         nums = [1] + nums + [1]
6
7         def dfs(l, r):
8            if l > r:
9                return 0
10            if (l, r) in dp:
11                return dp[(l, r)]
12            
13            dp[(l, r)] = 0
14            for i in range(l, r + 1):
15                coins = nums[l - 1] * nums[i] * nums[r + 1]
16                coins += dfs(l, i - 1) + dfs(i + 1, r)
17                dp[(l, r)] = max(dp[(l, r)], coins)
18            return dp[(l, r)]
19
20         return dfs(1, len(nums) - 2)