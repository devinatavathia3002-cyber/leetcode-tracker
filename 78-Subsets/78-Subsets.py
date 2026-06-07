# Last updated: 6/7/2026, 3:18:14 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        
4        output = [[]]
5
6        def recurse(i, curr):
7            nonlocal output
8
9            if i == len(nums):
10                return
11            
12            for j in range(i, len(nums)):
13                curr.append(nums[j])
14                recurse(j + 1, curr)
15                output.append(curr.copy())
16                curr.pop()
17
18        recurse(0, [])
19        return output