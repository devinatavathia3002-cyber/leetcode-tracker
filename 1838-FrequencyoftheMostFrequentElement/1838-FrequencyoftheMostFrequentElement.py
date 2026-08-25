# Last updated: 8/24/2026, 10:15:35 PM
1class Solution:
2    def maxFrequency(self, nums: List[int], k: int) -> int:
3        freq = 0
4        r, l = len(nums) - 1, len(nums) - 1
5        total = 0
6        
7        nums.sort()
8        while l >= 0:
9            total += nums[l]
10            freq = max(freq, r - l)
11            while ((nums[r] * (r - l + 1)) > total + k):
12                total -= nums[r]
13                r -= 1
14            l -= 1
15
16        freq = max(freq, r - l)
17        return freq