# Last updated: 2/11/2026, 10:00:46 PM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        
4        res = 0
5        currSum = 0
6
7        prefix = {0: 1}
8
9        for num in nums:
10            currSum += num
11
12            leftover = currSum - k
13
14            if leftover in prefix:
15                res += prefix[leftover]
16             
17            prefix[currSum] = (prefix.get(currSum, 0)) + 1
18        
19        return res