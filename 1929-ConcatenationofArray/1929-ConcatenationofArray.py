# Last updated: 2/17/2026, 11:37:17 PM
1class Solution:
2    def getConcatenation(self, nums: List[int]) -> List[int]:
3        
4        final = [0] * (2 * len(nums))
5        n = len(nums)
6
7        for i in range(n):
8            final[i] = nums[i]
9            final[i + n] = nums[i]
10        
11        return final
12