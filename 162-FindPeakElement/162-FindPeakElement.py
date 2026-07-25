# Last updated: 7/25/2026, 10:28:36 AM
1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3        l, r = 0, len(nums) - 1
4
5        while l <= r:
6            mid = ((r - l) // 2) + l
7            if ((mid == 0 or nums[mid] > nums[mid - 1]) and 
8                (mid == len(nums) - 1 or nums[mid] > nums[mid + 1])):
9                return mid
10            if mid > 0 and nums[mid] < nums[mid - 1]:
11                r = mid - 1
12            else:
13                l = mid + 1
14
15        return -1