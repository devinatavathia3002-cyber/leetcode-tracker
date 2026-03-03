# Last updated: 3/2/2026, 8:38:33 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        
4        # find the drop (point of rotation)
5        l = 0
6        r = len(nums) - 1
7        last = nums[r]
8
9        while l < r:
10            m = ((r - l) // 2) + l
11
12            if nums[m] > last:
13                l = m + 1
14            else:
15                r = m
16
17        return nums[r]