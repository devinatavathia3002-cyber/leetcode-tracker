# Last updated: 4/26/2026, 9:44:01 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        
4        # if len(nums) == 1:
5        #     return nums[0]
6        
7        # dp = [0] * len(nums)
8        # dp[0] = nums[0]
9        # dp[1] = max(nums[1], nums[0])
10
11        # for i in range(2, len(nums)):
12        #     # skip, or take it
13        #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
14        
15        # return dp[-1]
16
17        # now with no extra space
18
19        if len(nums) == 1:
20            return nums[0]
21        
22        first, second = nums[0], max(nums[1], nums[0])
23
24        for i in range(2, len(nums)):
25            temp = second
26            second = max(second, first + nums[i])
27            first = temp
28        
29        return second