# Last updated: 5/13/2026, 10:55:21 PM
1class Solution:
2    def findTargetSumWays(self, nums: List[int], target: int) -> int:
3        
4        # recursive solution
5        # def dfs(index, total):
6            
7        #     if total == target and index == len(nums):
8        #         return 1
9            
10        #     if index >= len(nums):
11        #         return 0
12            
13        #     return dfs(index + 1, total + nums[index]) + dfs(index + 1, total - nums[index])
14        
15        # return dfs(0, 0)
16
17        # dp solution
18
19        dp = defaultdict(int)
20        dp[0] = 1
21
22        for num in nums:
23            new = defaultdict(int)
24            for total, count in dp.items():
25                new[total + num] += count
26                new[total - num] += count
27            dp = new
28        
29        return dp[target]
30