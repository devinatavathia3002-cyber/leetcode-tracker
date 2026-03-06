# Last updated: 3/5/2026, 10:54:19 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> bool:
3        
4        l, r = 0, len(nums) - 1
5        
6        while l <= r:
7
8            m = ((r - l)//2) + l
9            print(m)
10
11            if nums[m] == target:
12                return m
13
14            elif nums[l] < nums[m]:
15                if nums[l] <= target < nums[m]:
16                    r = m - 1
17                else:
18                    l = m + 1
19            elif nums[l] > nums[m]:
20                if nums[m] < target <= nums[r]:
21                    l = m + 1
22                else:
23                    r = m - 1
24            else:
25                l += 1
26
27        return -1
28
29