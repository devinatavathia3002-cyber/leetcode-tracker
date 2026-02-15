# Last updated: 2/15/2026, 2:53:40 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        prefix = defaultdict(int)
4        suffix = defaultdict(int)
5
6        cumulative = 1
7        for i in range(len(nums)):
8            prefix[i] = cumulative
9            cumulative *= nums[i]
10        
11        multiply = 1
12        for i in range(len(nums) - 1, -1, -1):
13            suffix[i] = multiply
14            multiply *= nums[i]
15        
16        # final loop
17        for i in range(len(nums)):
18            nums[i] = (prefix[i] * suffix[i])
19        
20
21        return nums