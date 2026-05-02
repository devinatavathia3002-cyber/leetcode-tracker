# Last updated: 5/1/2026, 7:45:27 PM
1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        # def dfs(pre, index):
4        #     if index >= len(nums):
5        #         return 0
6        #     val = nums[index]
7        #     if val > pre:
8        #         return max(dfs(val, index + 1) + 1, dfs(pre, index + 1))
9        #     return dfs(pre, index + 1)
10        
11        # return dfs(float("-inf"), 0)
12
13        # with dp
14        dp = [1] * len(nums)
15
16        for i in range(len(nums) - 1, -1, -1):
17            curr = nums[i]
18            for j in range(i + 1, len(nums)):
19                if curr >= nums[j]:
20                    continue
21                dp[i] = max(dp[i], 1 + dp[j])
22
23        return max(dp)
24