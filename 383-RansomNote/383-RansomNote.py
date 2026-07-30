# Last updated: 7/29/2026, 9:47:31 PM
1class Solution:
2    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
3        charArr = [0] * 26
4
5        for char in ransomNote:
6            index = ord(char) - ord('a')
7            charArr[index] += 1
8        
9        for char in magazine:
10            index = ord(char) - ord('a')
11            charArr[index] -= 1
12        
13        for i in range(len(charArr)):
14            if charArr[i] > 0:
15                return False
16        
17        return True