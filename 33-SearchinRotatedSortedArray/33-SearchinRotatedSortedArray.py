# Last updated: 3/1/2026, 7:25:12 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l, r = 0, len(nums) - 1
4
5        while l < r:
6            m = ((r - l) // 2) + l
7            if nums[m] > nums[r]:
8                l = m + 1
9            else:
10                r = m
11
12        pivot = r
13        l, r = 0, len(nums) - 1
14
15        if target >= nums[pivot] and target <= nums[r]:
16            l = pivot
17        else:
18            r = pivot - 1
19
20        while l <= r:
21            m = ((r - l) // 2) + l
22            if nums[m] == target:
23                return m
24            elif nums[m] < target:
25                l = m + 1
26            else:
27                r = m - 1
28
29        return -1