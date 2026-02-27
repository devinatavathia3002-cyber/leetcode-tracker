# Last updated: 2/27/2026, 2:55:00 PM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        
4        nums = sorted(nums)
5        output = []
6
7        for i in range(len(nums)):
8
9            if nums[i] > 0:
10                break
11
12            # account for duplicate start vals
13            if i != 0 and nums[i] == nums[i - 1]:
14                continue
15            
16            l = i + 1
17            r = len(nums) - 1
18
19            target = (0 - nums[i])
20
21            while l < r:
22                add = nums[l] + nums[r]
23                if add > target:
24                    r -= 1
25                elif add < target:
26                    l += 1
27                else:
28                    subarr = [nums[i], nums[l], nums[r]]
29                    output.append(subarr)
30                    l += 1
31                    r -= 1
32                
33                while l < r and nums[l] == nums[l - 1] and l != (i + 1):
34                    l += 1
35
36        return output
37