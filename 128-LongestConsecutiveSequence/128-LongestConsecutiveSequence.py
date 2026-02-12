# Last updated: 2/11/2026, 8:12:02 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        
4        no_dupes = set(nums)
5        longest = 0
6
7        for num in no_dupes:
8            if (num - 1) not in no_dupes:
9                length = 1
10                count = 1
11                while (num + count) in no_dupes:
12                    length += 1
13                    count += 1
14                longest = max(length, longest)
15
16        return longest