# Last updated: 5/29/2026, 12:28:58 AM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        res = 0
4        for num in range(0, len(nums) + 1):
5            nums.append(num)
6        
7        for num in nums:
8            res = res ^ num
9
10        return res