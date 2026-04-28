# Last updated: 4/27/2026, 7:14:03 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3
4        if len(nums) < 4:
5            if len(nums) == 3:
6                return max(nums[1], max(nums[0], nums[2]))
7            if len(nums) == 2:
8                return max(nums[0], nums[1])
9            if len(nums) == 1:
10                return nums[0]
11        
12        def helper(start, end):
13            first = nums[start]
14            second = max(nums[start], nums[start + 1])
15
16            for i in range(start + 2, end):
17                temp = second
18                second = max(second, first + nums[i])
19                print(second)
20                first = temp
21            
22            return second
23
24        return max(helper(0, len(nums) - 1), helper(1, len(nums)))