# Last updated: 7/29/2026, 5:51:01 PM
1class Solution:
2    def compress(self, chars: List[str]) -> int:
3        # read, write, groupings
4        i, index, group = 0, 0, 0
5        
6        while i < len(chars):
7            while group < len(chars) and chars[i] == chars[group]:
8                group += 1
9            length = group - i
10            chars[index] = chars[i]
11            index += 1
12
13            if length > 1:
14                for j in range(len(str(length))):
15                    chars[index] = (str(length)[j])
16                    index += 1
17            i = group
18        
19        return index