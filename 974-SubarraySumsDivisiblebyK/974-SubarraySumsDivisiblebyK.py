# Last updated: 7/7/2026, 11:29:09 PM
1class Solution:
2    def subarraysDivByK(self, nums: List[int], k: int) -> int:
3        prefix = defaultdict(int)
4        currSum = 0
5        res = 0
6
7        prefix[0] = 1
8
9        for num in nums:
10            currSum += num
11            leftover = currSum % k
12
13            res += prefix[leftover]
14            prefix[leftover] += 1
15
16        return res