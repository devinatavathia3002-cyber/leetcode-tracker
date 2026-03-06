# Last updated: 3/5/2026, 7:14:07 PM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        
4        if len(nums) <= 1:
5            return nums
6
7        output = []
8        q = deque()
9
10        l = 0
11        r = 0
12
13        while (r - l + 1) <= k:
14            curr = nums[r]
15            while q and curr > nums[q[-1]]:
16                q.pop()
17            q.append(r)
18
19            r += 1
20        
21        r -= 1
22        output.append(nums[q[0]])
23
24        while r < len(nums) - 1:
25            while q and q[0] <= l:
26                q.popleft()
27
28            l += 1
29            r += 1
30
31            curr = nums[r]
32            while q and curr > nums[q[-1]]:
33                q.pop()
34            q.append(r)
35
36            output.append(nums[q[0]])
37
38        return output