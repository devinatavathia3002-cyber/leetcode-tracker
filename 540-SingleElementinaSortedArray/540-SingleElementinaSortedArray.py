# Last updated: 7/23/2026, 9:42:38 AM
1class Solution:
2    def singleNonDuplicate(self, nums: List[int]) -> int:
3        # binary search
4        l, r = 0, len(nums) - 1
5        while l <= r:
6            mid = ((r - l) // 2) + l
7            if ((mid + 1) == len(nums) or nums[mid + 1] != nums[mid]) and (mid == 0 or nums[mid - 1] != nums[mid]):
8                return nums[mid]
9            else:
10                if mid > 0 and nums[mid - 1] == nums[mid]:
11                    left = (mid - 1)
12                else:
13                    left = (mid)
14                if left % 2:
15                    r = mid - 1
16                else:
17                    l = mid + 1
18        return -1