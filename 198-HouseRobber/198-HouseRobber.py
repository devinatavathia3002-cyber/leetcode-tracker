# Last updated: 4/26/2026, 9:30:27 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        
4        if len(nums) == 1:
5            return nums[0]
6        
7        dp = [0] * len(nums)
8        dp[0] = nums[0]
9        dp[1] = max(nums[1], nums[0])
10
11        for i in range(2, len(nums)):
12            # skip, or take it
13            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
14        
15        return dp[-1]