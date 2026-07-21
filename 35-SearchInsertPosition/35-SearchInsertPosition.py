# Last updated: 7/20/2026, 7:57:55 PM
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        l, r = 0, len(nums) - 1
4
5        while l <= r:
6            mid = ((r - l) // 2) + l
7            val = nums[mid]
8
9            if target > val:
10                l = mid + 1
11            elif target < val:
12                r = mid - 1
13            else:
14                return mid
15
16
17        # target wasn't found
18        return l