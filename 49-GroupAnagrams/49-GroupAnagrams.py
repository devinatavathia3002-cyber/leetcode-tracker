# Last updated: 7/27/2026, 6:51:10 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3
4        # using a character map
5        mapping = defaultdict(list)
6
7        for string in strs:
8            charMap = [0] * 26
9            for char in string:
10                index = ord('a') - ord(char)
11                charMap[index] += 1
12            mapping[tuple(charMap)].append(string)
13        
14        output = []
15        for key, val in mapping.items():
16            output.append(val)
17        return output
18            
19        