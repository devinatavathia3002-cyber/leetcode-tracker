# Last updated: 7/14/2026, 9:01:52 PM
1class Solution:
2    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
3        
4        # dp = defaultdict(int)
5        # # recursive solution w/ cache
6        # def lines(i, j):
7        #     if i >= len(nums1) or j >= len(nums2):
8        #         return 0
9        #     if (i, j) in dp:
10        #         dp[(i, j)]
11            
12        #     if nums1[i] == nums2[j]:
13        #         dp[(i, j)] = 1 + lines(i + 1, j + 1)
14        #     else:
15        #         dp[(i, j)] = max(lines(i + 1, j), lines(i, j + 1))
16            
17        #     return dp[(i, j)]
18        
19        # return lines(0, 0)
20
21        # dp bottom-up
22
23        dp = [0] * (len(nums2) + 1)
24
25        for i in range(len(nums1)):
26            newDp = [0] * (len(nums2) + 1)
27            for j in range(1, len(nums2) + 1):
28                if nums1[i] == nums2[j - 1]:
29                    newDp[j] = 1 + dp[j - 1]
30                else:
31                    newDp[j] = max(newDp[j - 1], dp[j])
32            dp = newDp
33
34        return dp[-1]