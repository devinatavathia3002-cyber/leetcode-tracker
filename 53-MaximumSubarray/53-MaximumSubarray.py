# Last updated: 5/6/2026, 9:33:21 PM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        
4        if len(nums) <= 1:
5            return sum(nums)
6        
7        total = 0
8        best = nums[0]
9        for num in nums:
10            total = max(num, num + total)
11            best = max(total, best)
12
13        return best