# Last updated: 4/30/2026, 10:50:01 PM
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        res = max(nums)
4        maxi, mini = 1, 1
5
6        for num in nums:
7            if num == 0:
8                maxi, mini = 1, 1
9                continue
10            res = max(res, maxi * num, mini * num, num)
11
12            temp = maxi
13            maxi = max(maxi * num, mini * num, num)
14            mini = min(temp * num, mini * num, num)
15
16        return res