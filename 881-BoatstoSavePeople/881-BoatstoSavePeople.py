# Last updated: 2/14/2026, 2:33:57 AM
1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        
4        # implement count sort
5
6        maximum = max(people)
7        length = len(people)
8        count = [0] * (maximum + 1)
9
10        for num in people:
11            count[num] += 1
12        
13        pointer = 0 # pointer for count arr
14        for i in range(length):
15            while count[pointer] == 0:
16                pointer += 1
17            
18            people[i] = pointer
19            count[pointer] -= 1
20
21        # pair the weightiest person with least weighiest
22        l = 0
23        r = length - 1
24        output = 0
25
26        while l <= r:
27            leftover = (limit - people[r])
28
29            if people[l] <= leftover:
30                l += 1
31            
32            r -= 1
33            output += 1
34        
35        return output