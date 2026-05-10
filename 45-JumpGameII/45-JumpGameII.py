# Last updated: 5/9/2026, 8:12:41 PM
1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        
4        # greedy approach
5        r, l = 0, 0
6        n = len(nums)
7        steps = 0
8
9        while r < len(nums) - 1:
10            farthest = 0
11            for i in range(l, r + 1):
12                farthest = max(farthest, i + nums[i])
13            steps += 1
14            l = r + 1
15            r = farthest
16
17        return steps