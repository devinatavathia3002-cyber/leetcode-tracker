# Last updated: 7/11/2026, 7:20:18 PM
1class Solution:
2    def maxSubarraySumCircular(self, nums: List[int]) -> int:
3        currMax = 0
4        globalMax = nums[0]
5
6        currMin = 0
7        globalMin = nums[0]
8
9        total = 0
10
11        for num in nums:
12            currMax = max(num, num + currMax)
13            globalMax = max(globalMax, currMax)
14
15            currMin = min(num, num + currMin)
16            globalMin = min(globalMin, currMin)
17
18            total += num
19        
20        if (total - globalMin) == 0:
21            return globalMax
22        return max((total - globalMin), globalMax)