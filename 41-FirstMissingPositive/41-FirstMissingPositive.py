# Last updated: 7/2/2026, 9:10:24 PM
1class Solution:
2    def firstMissingPositive(self, nums: List[int]) -> int:
3        
4        maximum = len(nums) + 1
5        # convert all negative numbers to 0s, or anything inconsequential
6        for i in range(len(nums)):
7            if nums[i] <= 0:
8                nums[i] = maximum
9        
10        # use array as hashmap marking
11        for i in range(len(nums)):
12            curr = abs(nums[i])
13            if curr > 0 and curr < maximum:
14                if nums[curr - 1] > 0:
15                    nums[curr - 1] = -1 * nums[curr - 1]
16            else:
17                continue
18        
19        # return first missing positive
20        for i in range(1, len(nums) + 1):
21            if nums[i - 1] >= 0:
22                return i
23
24        return maximum