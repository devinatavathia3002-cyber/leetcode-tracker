# Last updated: 8/26/2026, 8:07:50 PM
1class Solution:
2    def minOperations(self, nums: List[int], x: int) -> int:
3
4        # [2, 2, 2, 3], x = 4
5        # recursive solution
6        # n = len(nums)
7        # output = float("inf")
8        # def findMin(r, l, leftover):
9        #     nonlocal output
10        #     if leftover == 0:
11        #         output = min(output, l + (n - 1 - r))
12        #         return
13        #     elif leftover < 0:
14        #         return
15        #     elif l > r:
16        #         return
17        #     else:
18        #         opt1, opt2 = nums[l], nums[r]
19        #         if opt1 > opt2:
20        #             if opt1 <= leftover:
21        #                 findMin(r, l + 1, leftover - opt1)
22        #             findMin(r - 1, l, leftover - opt2)
23        #         else:
24        #             if opt2 <= leftover:
25        #                 findMin(r - 1, l, leftover - opt2)
26        #             findMin(r, l + 1, leftover - opt1)
27                    
28        
29        # findMin(n - 1, 0, x)
30        # return output if output < float("inf") else -1
31
32        # sliding window sol
33
34        total, n = sum(nums), len(nums)
35        maxSize = -1
36
37        l, r = 0, 0
38        target = total - x
39        currTotal = 0
40
41        while r < len(nums):
42            currTotal += nums[r]
43
44            while l <= r and currTotal > target:
45                currTotal -= nums[l]
46                l += 1
47
48            if currTotal == target:
49                maxSize = max(maxSize, r - l + 1)
50            
51            r += 1
52
53        return n - maxSize if maxSize != -1 else -1