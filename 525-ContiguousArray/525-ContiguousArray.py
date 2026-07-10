# Last updated: 7/9/2026, 7:55:05 PM
1class Solution:
2    def findMaxLength(self, nums: List[int]) -> int:
3        res = 0
4        currSum = 0
5        prefix = defaultdict(int)
6        prefix[0] = -1
7
8        for i in range(len(nums)):
9            if nums[i] == 0:
10                nums[i] = -1
11        
12        for i in range(len(nums)):
13            curr = nums[i]
14            currSum += curr
15
16            if currSum in prefix:
17                res = max(res, (i - prefix[currSum]))
18            
19            if currSum not in prefix:
20                prefix[currSum] = i
21
22        return res