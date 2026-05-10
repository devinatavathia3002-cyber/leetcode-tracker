# Last updated: 5/9/2026, 6:52:15 PM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3
4        dp = [False] * len(nums)
5        dp[len(nums) - 1] = True
6
7        for i in range(len(nums) - 2, -1, -1):
8            val = nums[i]
9            if val != 0:
10                for j in range(i, i + val):
11                    if dp[j + 1] == True:
12                        dp[i] = True
13                        break
14        
15        return dp[0]
16        