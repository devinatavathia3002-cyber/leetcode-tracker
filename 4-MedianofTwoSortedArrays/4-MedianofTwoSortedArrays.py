# Last updated: 3/4/2026, 10:14:24 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        
4        # setup
5        if len(nums1) > len(nums2):
6            nums1, nums2 = nums2, nums1
7        
8        l, r = -1, len(nums1) - 1
9
10        length = len(nums1) + len(nums2)
11        halfway = (len(nums1) + len(nums2)) // 2
12
13        while True:
14
15            # indexes for nums1 and nums2
16            i = ((r - l) // 2) + l # nums1
17            j = halfway - i - 2 # nums2
18
19            Aright = nums1[i + 1] if i < len(nums1) - 1 else float("infinity")
20            Aleft = nums1[i] if i >= 0 else float("-infinity")
21            Bright = nums2[j + 1] if j < len(nums2) - 1 else float("infinity")
22            Bleft = nums2[j] if j >= 0 else float("-infinity")
23
24            if Aright >= Bleft and Aleft <= Bright:
25                if length % 2 == 0:
26                    return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
27                else:
28                    return min(Aright, Bright)
29            
30            if Aright < Bleft:
31                l = i + 1
32            else:
33                r = i - 1
34            
35
36        
37