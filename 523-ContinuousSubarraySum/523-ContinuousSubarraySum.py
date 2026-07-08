# Last updated: 7/7/2026, 11:57:07 PM
1class Solution:
2    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
3        prefix = defaultdict(int)
4        prefix[0] = -1
5        currSum = 0
6
7        for i, num in enumerate(nums):
8            currSum += num
9            leftover = currSum % k
10
11            if leftover in prefix and (i - prefix[leftover]) > 1:
12                return True
13            
14            if leftover not in prefix:
15                prefix[leftover] = i
16
17        return False